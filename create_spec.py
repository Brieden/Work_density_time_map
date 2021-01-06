import yaml
import json
from jinja2 import Environment, FileSystemLoader
import ast

# Load input from user
config_data = yaml.load(open('template/data_to_feed.yml'), Loader=yaml.FullLoader)
env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)

# Load template
template = env.get_template('template/template.txt')

# Render input to template
output_from_parsed_template=(template.render(config_data))

# Save generated .yaml file
with open('pipeline-spec.yaml', "w") as fh:
    fh.write(output_from_parsed_template)

