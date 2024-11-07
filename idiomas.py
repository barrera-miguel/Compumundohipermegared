import json


def load_language(language_code):
    try:
        with open(f"{language_code}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Language file for '{language_code}' not found.")
        return {}
    
def idioma(language_code):
    texts = load_language(language_code)
    return texts