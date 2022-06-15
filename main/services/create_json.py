import json
from parser.models import Site


def main():
    database = list(Site.objects.values('organisation', 'phone', 'website', 'email', 'address', 'thematic', 'city', 'state'))
    with open('full_database.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(database))
    return True