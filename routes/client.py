from fastapi import APIRouter

page_router = APIRouter()

@page_router.get("/")
async def home():
    return {"message": "we are on home page"}

@page_router.get("/about")
async def about():
    return {"message": "we are on about page"}