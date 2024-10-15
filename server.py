from fastapi import FastAPI
import uvicorn
import socket
from pydantic import BaseModel

app = FastAPI()

class SongCreate(BaseModel):
    song_name: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

#Holder for 
songs = []

@app.post("/request/")
async def store_song(song_name: SongCreate):
    return {"song": "Anything"}
    # return {"message": f"Song '{song}' stored successfully", "total_songs": len(songs)}

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    uvicorn.run(app, host=ip_address, port=8080)


