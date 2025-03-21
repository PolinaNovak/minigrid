import json

def save_config(**kwargs):
    config = kwargs
    with open('config_for_student.json', 'w') as file:
        json.dump(config, file, indent=4)
