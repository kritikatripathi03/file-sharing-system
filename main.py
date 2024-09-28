from fastapi import FastAPI
from routes.client import page_router

app = FastAPI()

#@app.get('/health')
#async def health():
#    return {"status": "ok"}

def include_router(app):
    app.include_router(page_router)

def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()