import json

def save_statistics(filename, data):
    with open(filename, mode='w') as file:
        json.dump(data, file)
