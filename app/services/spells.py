import requests

class HPSpellService:
    API_URL = "https://hp-api.onrender.com/api/spells"

    def get_spells(self, limit=10):
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            return response.json()[:limit]
        except requests.RequestException as e:
            print(f"Error obtenint encanteris: {e}")
            return []
