
seen_strings = {}

def stringinate():
    while True:
        inputResult = input('Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')
        if (inputResult.lower() == "quit"):
            print('Exiting...\n')
            break
        elif (inputResult.lower() == "stats"):
            print('\nStats:\n %s\n' % seen_strings)
        else:
            print('\nInput = %s' % inputResult)
            print('Length = %s \n' % len(inputResult))

            if inputResult in seen_strings:
                seen_strings[inputResult] += 1
            else:
                seen_strings[inputResult] = 1

if __name__ == '__main__':
    stringinate()