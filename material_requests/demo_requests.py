import requests


## https://catfact.ninja/
def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    return response.json()      

cat_fact = get_cat_fact()
print(cat_fact)


def get_cat_facts():
    url = "https://catfact.ninja/facts"
    params = {"limit": 5}
    response = requests.get(url, params=params)
    return response.json()

cat_facts = get_cat_facts()
print(cat_facts)



def post_json_placeholder():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Test Post",
        "body": "Dieser Post zeigt, wie ein POST-Request funktioniert.",
        "userId": 1
    }

    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

post_json_placeholder()


def put_json_placeholder():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "title": "Aktualisierter Post",
        "body": "Dieser Post wurde mit einer PUT-Anfrage aktualisiert.",
        "userId": 1
    }

    response = requests.put(url, json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

put_json_placeholder()


def get_random_number_fact():
    response = requests.get("http://numbersapi.com/random/trivia")
    return response.text

random_number_fact = get_random_number_fact()
print(random_number_fact)


def get_number_facts():
    url = "http://numbersapi.com/42/trivia"
    response = requests.get(url)
    return response.text

number_facts = get_number_facts()
print(number_facts)


def get_nasa_apod():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "DEMO_KEY",
        "date": "2022-01-01"
    }

    response = requests.get(url, params=params)
    return response.json()

nasa_apod = get_nasa_apod()
print(nasa_apod)


def get_multiple_choice_facts():
    url = "https://opentdb.com/api.php"
    params = {
        "amount": 5,
        "category": 9,
        "difficulty": "easy",
        "type": "multiple"
    }

    response = requests.get(url, params=params)
    return response.json()

multiple_choice_facts = get_multiple_choice_facts()
print(multiple_choice_facts)


import dotenv
import os
dotenv.load_dotenv()

# zum Ausführen ist ein GITHUB_ACCESS_TOKEN in der .env Datei erforderlich
def get_github_user_info():
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    url = "https://api.github.com/users/octocat"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

github_user_info = get_github_user_info()
print(github_user_info)
