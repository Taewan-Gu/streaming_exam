from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/")
def main():
    file_like = open("hi.mp4", mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)