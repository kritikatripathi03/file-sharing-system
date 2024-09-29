from fastapi import FastAPI
from routes import ops, client
import os
from db.base import Base
from db.session import engine

app = FastAPI()

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI()
    app.include_router(ops.router, prefix="/ops", tags=["Ops User"])
    app.include_router(client.router, prefix="/client", tags=["Client"])
    create_tables()
    return app

app = start_application()

# Serve uploaded files
@app.get("/uploads/{filename}")
def get_uploaded_file(filename: str):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return {"message": "File not found"}
    return {"file_path": file_path}
