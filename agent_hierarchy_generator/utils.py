import yaml

def write_yaml_to_file(data, filename):
    with open(filename, 'w') as f:
        yaml.dump(data, f)