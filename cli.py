import requests
from requests.models import Response

def stats():
    response: Response = requests.get('http://127.0.0.1:5000/stats')
    print(response.text)

def add(s: str):
    response: Response = requests.post('http://127.0.0.1:5000/add', json={"string": s})

def cli_runner():
    while True:
        input_result = input('Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')
        if (input_result.lower() == "quit"):
            print('Exiting...\n')
            break
        elif (input_result.lower() == "stats"):
            stats()
        else:
            add(input_result)

if __name__ == '__main__':
    cli_runner()