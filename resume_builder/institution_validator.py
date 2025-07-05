import os
import requests
from dotenv import load_dotenv
from prompt_toolkit import prompt

load_dotenv()
SCORECARD_API_KEY = os.getenv("SCORECARD_API_KEY")

class Institution_Validator:
    BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

    def __init__(self):
        self.cache = {}
        if not SCORECARD_API_KEY:
            raise ValueError("Missing SCORECARD_API_KEY in environment variables")

    def validate(self, name):
        key = name.strip().lower()

        if key in self.cache:
            return self.cache[key]

        result = self.validate_from_api(key)
        self.cache[name] = result
        return result

    def validate_from_api(self, name):
        params = {
            "api_key": SCORECARD_API_KEY,
            "school.name": name,
            "fields": "id,school.name,school.city,school.state,school.school_url",
            "per_page": 100
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout = 5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Network/API issue: {e}")
            return None

        data = response.json()
        results = data.get("results", [])
        if not results:
            print(f"Not matching instutions found matching {name}")
            return None

        if len(results) > 1:
            print("Did you mean the following schools?")
            for i, school in enumerate(results):
                print(f"{i}. {school["school.name"]}")

            while True:
                choice = prompt("Enter the number of the correct institution or enter to cancel ")
                if choice == "":
                    print("Institution selection cancelled")
                    return None
                elif choice.isdigit() and 0 <= int(choice) < len(results):
                    return results[int(choice)]
                else:
                    print("Invalid selection")
        else:
            return results[0]
