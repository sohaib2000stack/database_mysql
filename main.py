from app.v1 import router as app
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True, host="0.0.0.0", port=8000)
