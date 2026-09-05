import requests
def get_steam_app_info(app_id):
    # URL для получения данных об игре
    # Используем эндпоинт _javascript_, так как он часто возвращает данные в удобном формате
    url = f"http://api.steampowered.com/ISteamApps/GetAppDetails/app{app_id}/_javascript_"
    try:
        response = requests.get(url)
        # Проверяем, успешно ли прошел запрос
        if response.status_code == 200:
            data = response.json()
            # Данные в Steam API часто приходят в виде словаря с ключом 'data'
            # Структура может немного отличаться в зависимости от игры
            app_data = data.get('data', {})
            name = app_data.get('name', 'Не найдено')
            description = app_data.get('description', 'Описание отсутствует')
            print(f"Название игры: {name}")
            print(f"Описание: {description}")
            # Если нужно вывести все данные в сыром виде:
            # print(data)
        else:
            print(f"Ошибка запроса: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
# Пример: ID игры Counter-Strike 2 (730)
app_id = "730"
get_steam_app_info(app_id)
