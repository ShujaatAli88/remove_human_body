from fastapi import FastAPI
from .api.endpoints import router as api_router
from .config import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI(title=settings.PROJECT_NAME,
               version=settings.PROJECT_VERSION,
               description="API for segmenting clothing items in images")

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(api_router, prefix="/api/v1")

if __name__ =="__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
