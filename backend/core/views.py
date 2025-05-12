from django.http import HttpResponse
from django.db import connection
def home(request):
    current_schema = connection.schema_name
    return HttpResponse(f"Hello from schema: {current_schema}")
