from . import db
import json

def get_cityes_and_states() -> dict:
    with open('cityes.json', 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def main(queryes: list[str] = ['car repair service'], mode: int = 0, ignore_processed_cityes: bool = True):
    states_and_cityes = get_cityes_and_states()
    for query in queryes:
        mine_data = []
        if mode == 0:
            db.add_query(query=query, city=None, state=None)
        elif mode == 1:
            for state in states_and_cityes:
                for city in states_and_cityes[state]:
                    city = city.title()
                    is_exist = False
                    if ignore_processed_cityes:
                        is_exist = db.is_city_exist_in_db(city, state)
                    if not is_exist:
                        q = f"{query} near {city}, {state}"
                        db.add_query(query=q, city=city, state=state)
                    else:
                        print(f'Drop {city}')
        elif mode == 2:
            for state in states_and_cityes:
                q = f"{query} near {state}"
                db.add_query(query=q, city=None, state=state)
        else:
            return 0
    return True
    
