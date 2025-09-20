from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Uzbek Songs API", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MP3 fayllar saqlanadigan papka
app.mount("/songs", StaticFiles(directory="songs"), name="songs")


class Song(BaseModel):
    id: int
    title: str
    artist: str
    year: int
    url: str
    img:str


SONGS = [
    {"id": 1,
     "title": "Yalla – Ulug‘imsan vatanim",
     "artist": "Yalla",
     "year": 2020,
     "url": "https://musicapi-2gws.onrender.com/songs/1.mp3",
     "img": "https://musicapi-2gws.onrender.com/songs/images/1.jpg"},
    {"id": 2, 
    "title": "Sherali Jo‘rayev – O‘zbegim",
     "artist": "Sherali Jo‘rayev", "year": 2020,
     "url": "https://musicapi-2gws.onrender.com/songs/2.mp3", 
     "img": "https://musicapi-2gws.onrender.com/images/2.jpg"},
    {"id": 3, "title": "Sevara Nazarkhan – Yor-yor", "artist": "Sevara Nazarkhan", "year": 2021,
     "url": "https://musicapi-2gws.onrender.com/songs/3.mp3", "img": "https://musicapi-2gws.onrender.com/images/3.jpg"},
    {"id": 4, "title": "Yulduz Usmonova – Vatan", "artist": "Yulduz Usmonova", "year": 2021,
     "url": "https://musicapi-2gws.onrender.com/songs/4.mp3", "img": "https://musicapi-2gws.onrender.com/images/4.jpg"},
    {"id": 5, "title": "Ozodbek Nazarbekov – Qora ko‘zlaring", "artist": "Ozodbek Nazarbekov", "year": 2022,
     "url": "https://musicapi-2gws.onrender.com/songs/5.mp3", "img": "https://musicapi-2gws.onrender.com/images/5.jpg"},
    {"id": 6, "title": "Shahzoda – Kerak emas", "artist": "Shahzoda", "year": 2022,
     "url": "https://musicapi-2gws.onrender.com/songs/6.mp3", "img": "https://musicapi-2gws.onrender.com/images/6.jpg"},
    {"id": 7, "title": "Ulug‘bek Rahmatullayev – Sensiz", "artist": "Ulug‘bek Rahmatullayev", "year": 2022,
     "url": "https://musicapi-2gws.onrender.com/songs/7.mp3", "img": "https://musicapi-2gws.onrender.com/images/7.jpg"},
    {"id": 8, "title": "Munisa Rizayeva – Sevgi iztirobi", "artist": "Munisa Rizayeva", "year": 2022,
     "url": "https://musicapi-2gws.onrender.com/songs/8.mp3", "img": "https://musicapi-2gws.onrender.com/images/8.jpg"},
    {"id": 9, "title": "Lola – Ko‘nikmadim", "artist": "Lola", "year": 2023,
     "url": "https://musicapi-2gws.onrender.com/songs/9.mp3", "img": "https://musicapi-2gws.onrender.com/images/9.jpg"},
    {"id": 10, "title": "Shoxrux – Hayot", "artist": "Shoxrux", "year": 2023,
     "url": "https://musicapi-2gws.onrender.com/songs/10.mp3", "img": "https://musicapi-2gws.onrender.com/images/10.jpg"},
    {"id": 11, "title": "Rayhon – Baxtli bo‘laman", "artist": "Rayhon", "year": 2023,
     "url": "https://musicapi-2gws.onrender.com/songs/11.mp3", "img": "https://musicapi-2gws.onrender.com/images/11.jpg"},
    {"id": 12, "title": "Jahongir Otajonov – Ona", "artist": "Jahongir Otajonov", "year": 2023,
     "url": "https://musicapi-2gws.onrender.com/songs/12.mp3", "img": "https://musicapi-2gws.onrender.com/images/12.jpg"},
    {"id": 13, "title": "Sardor Rahimxon – Yomg‘ir", "artist": "Sardor Rahimxon", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/13.mp3", "img": "https://musicapi-2gws.onrender.com/images/13.jpg"},
    {"id": 14, "title": "Nilufar Usmonova – Jonim", "artist": "Nilufar Usmonova", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/14.mp3", "img": "https://musicapi-2gws.onrender.com/images/14.jpg"},
    {"id": 15, "title": "Manzura – Kel sevgilim", "artist": "Manzura", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/15.mp3", "img": "https://musicapi-2gws.onrender.com/images/15.jpg"},
    {"id": 16, "title": "Ziyoda – Sen ketma", "artist": "Ziyoda", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/16.mp3", "img": "https://musicapi-2gws.onrender.com/images/16.jpg"},
    {"id": 17, "title": "Shohruhxon – Sevgi haqida", "artist": "Shohruhxon", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/17.mp3", "img": "https://musicapi-2gws.onrender.com/images/17.jpg"},
    {"id": 18, "title": "Shahriyor – Yorim seni", "artist": "Shahriyor", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/18.mp3", "img": "https://musicapi-2gws.onrender.com/images/18.jpg"},
    {"id": 19, "title": "Xurshid Rasul – Xotira", "artist": "Xurshid Rasul", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/19.mp3", "img": "https://musicapi-2gws.onrender.com/images/19.jpg"},
    {"id": 20, "title": "Farrux Raimov – Dil izhori", "artist": "Farrux Raimov", "year": 2024,
     "url": "https://musicapi-2gws.onrender.com/songs/20.mp3", "img": "https://musicapi-2gws.onrender.com/images/20.jpg"},
]


@app.get("/songs", response_model=List[Song])
def get_songs():
    return SONGS


@app.get("/songs/{song_id}", response_model=Song)
def get_song(song_id: int):
    for song in SONGS:
        if song["id"] == song_id:
            return song
    return {"error": "Qo'shiq topilmadi"}
