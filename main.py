from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError
from app.routers import user_router, auth_router
from app.core.exception_handler import http_exception_handler, validation_exception_handler
from fastapi.middleware.cors import CORSMiddleware
import logging


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router.router, prefix="/users", tags=["users"])

app.include_router(api_router)
