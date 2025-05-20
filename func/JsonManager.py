import json

# Класс взаимодействия с внешними json файлами
class JsonManager:

    def __init__(self,m):
        
        # Загрузка конфигурации
        m.config = self.load('config')

    # Функция получения информации
    def load(self, path:str):
        
        try:

            with open(f'{path}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            return data

        except Exception as err:
            print(f'[Error][JsonManager][Load]: {err}')

    # Функция сохранения информации
    def save(self, path:str, data: any):
        
        try:
          
            with open(f'{path}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception as err:
            print(f'[Error][JsonManager][Save]: {err}')