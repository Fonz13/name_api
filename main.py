from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from routers import get_name
from fastapi_utils.tasks import repeat_every
import requests

# from config import settings

app = FastAPI()


@app.get("/")
def root():
    return "Welcome to my name game API! use the /docs endpoint to see the docs"


@app.on_event("startup")
@repeat_every(seconds=60)  # 1 minute
def remove_expired_tokens_task() -> None:
    x = requests.get(
        "https://name-game-hdxh.onrender.com/search_name/", params={"name": "Fonzie"}
    )
    print(x.text)


app.include_router(get_name.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
