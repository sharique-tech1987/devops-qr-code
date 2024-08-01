from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from . import api_router

# Loading Environment variable (AWS Access Key and Secret Key)
load_dotenv()

app = FastAPI()
# Mount the API router to the main app
app.include_router(api_router.router)

# Allowing CORS for local testing
origins = [
    os.getenv("BASE_URL") + ":" + os.getenv("PORT") 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

