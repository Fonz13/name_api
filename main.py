from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from routers import get_name

# from config import settings

app = FastAPI()


# origins = settings.BACKEND_CORS_ORIGINS


app.include_router(get_name.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
