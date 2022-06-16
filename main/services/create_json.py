import json
from parser.models import Site


def main():
    database = list(Site.objects.values('organisation', 'phone', 'website', 'email', 'address', 'thematic', 'city', 'state', 'query'))
    name = './full_database.json'
    with open(name, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(database))
    return name