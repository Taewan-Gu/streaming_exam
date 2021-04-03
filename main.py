from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

route = "hi2.m3u8"
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    file_like = open(route, mode="rb")
    return StreamingResponse(file_like, media_type="application/vnd.apple.mpegurl")

@app.get("/a")
def madficssfsdnh():
    file_like = open(route, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

@app.get("/b")
def madfissfsdnh():
    file_like = open(route, mode="rb")
    return StreamingResponse(file_like, media_type="application/x-mpegurl")

@app.get("/c")
def madfisfsfddnh():
    file_like = open(route, mode="rb")
    return StreamingResponse(file_like, media_type="audio/mpegurl")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8082, reload=True)