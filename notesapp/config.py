from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLITE_DB_URL = "sqlite:///db/notesdb.db"
    PROJECT_NAME = "NotesAPP"
    PROJECT_VERSION = "0.0.1"


settings = Settings()
