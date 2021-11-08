import requests

def stats():
    print("stats")

def add(s: str):
    print("add")

def cli_runner():
    while True:
        input_result = input('Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')
        if (input_result.lower() == "quit"):
            print('Exiting...\n')
            break
        elif (input_result.lower() == "stats"):
            stats()
        else:
            add("hi")

if __name__ == '__main__':
    cli_runner()