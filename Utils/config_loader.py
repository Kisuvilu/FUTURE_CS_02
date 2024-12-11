import yaml
import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.yaml'):
            return yaml.safe_load(file)
        elif file_path.endswith('.json'):
            return json.load(file)
        else:
            raise ValueError("Unsupported configuration format")
