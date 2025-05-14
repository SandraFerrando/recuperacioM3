import requests

class HPCharacterService:
    API_URL = "https://hp-api.onrender.com/api/characters"

    def get_characters(self, limit=5):
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            return response.json()[:limit]
        except requests.RequestException as e:
            print(f"Error obtenint personatges: {e}")
            return []
