from django.core.management.base import BaseCommand
from django_tenants.utils import tenant_context
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from core.models import Client

class Command(BaseCommand):
    help = 'Create default groups and assign permissions for all tenants'

    def handle(self, *args, **options):
        for client in Client.objects.all():
            with tenant_context(client):
                self.stdout.write(f"Processing tenant: {client.schema_name}")
                
                # Create groups from TENANT_USER_ROLES
                for role, role_name in settings.TENANT_USER_ROLES:
                    group, created = Group.objects.get_or_create(name=role)
                    if created:
                        self.stdout.write(f"Created group: {role} for tenant {client.schema_name}")
                    else:
                        self.stdout.write(f"Group {role} already exists for tenant {client.schema_name}")

                    # Assign department-specific permissions
                    if role == 'finance_manager':
                        permissions = Permission.objects.filter(
                            content_type__app_label='finance'
                        )
                        group.permissions.set(permissions)
                        self.stdout.write(f"Assigned finance permissions to {role}")
                    
                    elif role == 'human_resource_manager':
                        permissions = Permission.objects.filter(
                            content_type__app_label='hrm'
                        )
                        group.permissions.set(permissions)
                        self.stdout.write(f"Assigned hrm permissions to {role}")
                    
                    elif role == 'inventory_manager':
                        permissions = Permission.objects.filter(
                            content_type__app_label='inventory'
                        )
                        group.permissions.set(permissions)
                        self.stdout.write(f"Assigned inventory permissions to {role}")
                    
                    elif role == 'administrator':
                        # Administrator gets all permissions across apps
                        permissions = Permission.objects.filter(
                            content_type__app_label__in=['finance', 'hrm', 'inventory']
                        )
                        group.permissions.set(permissions)
                        self.stdout.write(f"Assigned all permissions to {role}")

        self.stdout.write(self.style.SUCCESS("Successfully created default groups and permissions for all tenants"))