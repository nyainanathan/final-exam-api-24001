from fastapi import FastAPI
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
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

cars : List[CarPayload] = []
@app.post("/cars")
def create_cars(new_cars: List[CarPayload]):
    cars.extend(new_cars)
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

@app.put("/cars/{id}/characteristics")
def update_characteristics(id: int, characteristics_updated: Characteristics):
    for car in cars:
        if car.id == id:
            car.characteristics = characteristics_updated
            return JSONResponse(content={"car": car}, status_code=200)
    return JSONResponse(content={"Message": "We don't have data on the car you are searching"}, status_code=404)

