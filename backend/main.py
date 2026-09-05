import requests
import time
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Разрешаем фронтенду обращаться к бэкенду (CORS)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
#grigoriy
APP_ID = 252490
input_cur="ru"

def get_regional_prices(appid,cur):
    print(f"=== Сбор региональных цен для AppID: {appid} ===")
    # Формируем URL с параметром конкретной страны (cc)
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc={cur}"
    characteristics = ("name", "price_overview", "about_the_game", "supported_languages", "website",
                           "pc_requirements")
    try:
        response = requests.get(url)
        data = response.json()
        if data and data[str(appid)]['success']:
            game_info = {
                "name": data[str(appid)]['data']['name'],
                "price": data[str(appid)]['data']["price_overview"].get('final_formatted'),
                "currency": data[str(appid)]['data']["price_overview"].get('currency'),
                'discount_percent': data[str(appid)]['data']["price_overview"].get('discount_percent'),
                "about_the_game": data[str(appid)]['data']["about_the_game"],
            }
            return (game_info)

    except Exception as e:
        return(f"error {cur}: {e}")
        # Небольшая пауза, чтобы Steam не заблокировал за частые запросы


@app.get("/api/games")

def get_games():
    return json.dumps(get_regional_prices(APP_ID,input_cur))
