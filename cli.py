import requests
from requests.models import Response

def stats():
    response: Response = requests.get('http://127.0.0.1:5000/stats')
    print(response.text)

def add(s: str):
    response: Response = requests.post('http://127.0.0.1:5000/add', json={"string": s})

def to_csv(csv_path: str):
    response: Response = requests.post('http://127.0.0.1:5000/to_csv', json={"csv_path": csv_path})

def from_csv(csv_path: str):
    response: Response = requests.post('http://127.0.0.1:5000/from_csv', json={"csv_path": csv_path})

def cli_runner():
    while True:
        input_result = input('Enter an input string (\'stats\' to see statistics, \'to_csv\' to write strings to csv, \'from_csv\' to load strings from csv, \'quit\' to exit): ')
        if (input_result.lower() == "quit"):
            print('Exiting...\n')
            break
        elif (input_result.lower() == "stats"):
            stats()
        elif (input_result.lower() == "to_csv"):
            csv_path = input('Enter path to output csv file: ')
            to_csv(csv_path)
        elif (input_result.lower() == "from_csv"):
            csv_path = input('Enter path to input csv file: ')
            from_csv(csv_path)
        else:
            add(input_result)

if __name__ == '__main__':
    cli_runner()