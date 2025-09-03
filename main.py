from fastapi import FastAPI
import base64
from _pydatetime import datetime
from fastapi import FastAPI
from pydantic_core.core_schema import DatetimeSchema
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List
app = FastAPI()


@app.get("/ping")
def root():
    return Response(content="pong", status_code=200, media_type="text/plain")

class Characteristics(BaseModel):
    max_speed: int
    max_fuel_capacity: int

class CarPayload(BaseModel):
    indentifier: str
    brand: str
    model: str
    characteristics: Characteristics

cars : List[CarPayload] = []
@app.post("/cars")
def create_cars(newCars: List[CarPayload]):
    cars.extend(newCars)
    return JSONResponse(content={"cars": cars}, status_code=201)

@app.get("/cars")
def get_cars():
    required_cars = []
    for car in cars:
        required_cars.append(car.model_dump())
    return JSONResponse(content={"cars": required_cars}, status_code=200)

@app.get("/cars/{id}")
def get_car(id: int):
    for car in cars:
        if car.id == id:
            return JSONResponse(content={"car": car}, status_code=200)
    return JSONResponse(content={"Message": "We don't have data on the car you are searching"}, status_code=404)


