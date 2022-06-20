from ..models import QueryesPool, Site as SiteModel
from django.db.utils import DataError, IntegrityError
from django.db import transaction

def is_website_exist_in_db(website: str):
    return SiteModel.objects.filter(website=website).exists()

def is_city_exist_in_db(city: str, state: str):
    return SiteModel.objects.filter(city=city, state=state).exists()

def write_to_site_db(database: list) -> bool:
    for card in database:
        try:
            with transaction.atomic():
                s = SiteModel(
                    organisation=card['name'],
                    thematic=card['thematic'],
                    email=card['email'],
                    phone=card['phone'],
                    website=card['website'],
                    state=card['state'],
                    city=card['city'],
                    address=card['address'],
                    query=card['query']
                )
                s.save()
        except IntegrityError:
            pass
            
        except DataError:
            pass
    return True

def add_query(query: str, city: str | None, state: str | None) -> bool:
    try:
        with transaction.atomic():
            s = QueryesPool(
                query=query,
                city=city,
                state=state
            )
            s.save()
            return True
    except IntegrityError:
        pass
    except DataError:
        pass
    
def get_any_query() -> dict | None:
    instance = QueryesPool.objects.all().first()
    if instance:
        result = {
            'query': instance.query,
            'city': instance.city,
            'state': instance.state
        }
        instance.delete()
        return result
    
    