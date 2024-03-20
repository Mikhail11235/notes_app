from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from db.base_class import Base
from db.session import engine
from api.base import api_router


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    Base.metadata.create_all(bind=engine)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    return app


app = start_application()
