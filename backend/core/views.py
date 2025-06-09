from django.http import HttpResponse
from django.db import connection
from django_tenants.utils import schema_context
def home(request):
    current_schema = connection.schema_name
    return HttpResponse(f"Hello from schema: {current_schema}")



def get_all_users_across_tenants():
    from users.models import CustomUser
    users = []
    from core.models import Client
    for client in Client.objects.all():
        with schema_context(client.schema_name):
            users += list(CustomUser.objects.all())
    return users
