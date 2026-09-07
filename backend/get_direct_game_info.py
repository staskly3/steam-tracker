import requests
import time
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import game_id
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_regional_prices(cur):
    info=[]
    for i in range(0,len(game_id.idies.values())):
        print(f"Сбор региональных цен для AppID: {str(list(game_id.idies.values())[i])} ===")
        url = f"https://store.steampowered.com/api/appdetails?appids={str(list(game_id.idies.values())[i])}&cc={cur}"
        try:
            print(i)
            response = requests.get(url)
            data = response.json()
            if data and data[str(list(game_id.idies.values())[i])]['success']:
                game_data = data[str(list(game_id.idies.values())[i])]['data']
                info.append({
                    "name": game_data.get('name'),
                    "price": game_data.get('price_overview', {}).get('final_formatted'),
                    "currency": game_data.get('price_overview', {}).get('currency'),
                    'discount_percent': game_data.get('price_overview', {}).get('discount_percent'),
                    "about_the_game": "info"#game_data.get("about_the_game"),  # Твой плейсхолдер
                })

        except Exception as e:
            return(f"error {cur}: {e}")
    for _ in range(len(info)):
        print(_,info[_])

@app.get("/api/games")

def get_games(country: str = None):#appid: str = None,
    return (get_regional_prices(str(country)))
print(get_games("ru"))
