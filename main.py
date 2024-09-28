from fastapi import FastAPI
from routes.client import page_router

from db.base import Base
from db.session import engine

app = FastAPI()

#@app.get('/health')
#async def health():
#    return {"status": "ok"}

def include_router(app):
    app.include_router(page_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI()
    include_router(app)
    create_tables()
    return app

app = start_application()