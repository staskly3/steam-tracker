import requests
import time
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
APP_ID = 252490
input_cur="ru"

def get_regional_prices(appid,cur):
    print(f"Сбор региональных цен для AppID: {appid} ===")
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc={cur}"
    characteristics = ("name", "price_overview", "about_the_game", "supported_languages", "website",
                           "pc_requirements")
    try:
        response = requests.get(url)
        data = response.json()
        if data and data[str(appid)]['success']:
            x=""
            j=0
            game_data = data[str(appid)]['data']
            game_info = {
                "name": game_data.get('name'),
                "price": game_data.get('price_overview', {}).get('final_formatted'),
                "currency": game_data.get('price_overview', {}).get('currency'),
                'discount_percent': game_data.get('price_overview', {}).get('discount_percent'),
                "about_the_game": "info"#game_data.get("about_the_game"),  # Твой плейсхолдер
            }

            return (game_info)

    except Exception as e:
        return(f"error {cur}: {e}")

@app.get("/api/games")

def get_games(country: str = None):#appid: str = None,
    return (get_regional_prices(APP_ID,str(country)))