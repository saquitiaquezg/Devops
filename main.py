import request

def get_weather();
    result = requests.get("www.ambiente.com/api")
    return result.json()["Temperature"]