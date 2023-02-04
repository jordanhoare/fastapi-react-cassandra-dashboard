# flake8: noqa

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.router import api_router
from app.core import get_settings
from app.db import create_session

settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logging.raiseExceptions = False
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime} @ {filename}->{funcName}:{lineno} : {message}",
        style="{",
        use_colors=True,
    )
    logger.handlers[0].setFormatter(console_formatter)
    # logger.propagate = False


@app.on_event("shutdown")
async def shutdown_event():
    pass


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_DEBUG_MODE,
        workers=settings.SERVER_WORKERS,
    )
