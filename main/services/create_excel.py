from parser.services.excel import write_to_excel
from parser.models import Site

def main():
    database = list(Site.objects.values('organisation', 'phone', 'website', 'email', 'address', 'thematic', 'city', 'state'))
    write_to_excel(database=database, name='./full_database.xlsx')
    return True