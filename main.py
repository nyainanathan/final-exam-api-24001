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