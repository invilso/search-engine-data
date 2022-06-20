from ..models import QueryesPool

def get_html():
    html = f'<h1>Left {QueryesPool.objects.all().count()} queryes</h1>'
    return html