from .google_search import search

def main():
    data = []
    for v in search('Automotive workshops', num_results=100):
        data.append(v)
    return data
