from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import socket
from pydantic import BaseModel

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

class SongCreate(BaseModel):
    song_name: str


#@app.get("/")
#async def root():
    

#Holder for 
songs = []

@app.post("/request")
async def store_song(song_name: SongCreate):
    return {"song": "Anything"}
    # return {"message": f"Song '{song}' stored successfully", "total_songs": len(songs)}

@app.post("/search")
async def search_song(song_name: SongCreate):
    print("TRIED")
    return {"song": "SEARCH"}

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    uvicorn.run(app, host=ip_address, port=8080)


