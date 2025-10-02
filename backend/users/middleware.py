from django.http import HttpResponseForbidden

# users/middleware.py

class TenantAccessMiddleware:
    """
    Ensures that tenant users can only access their own tenant.
    Works with django-tenants 3.x+.
    Assumes TenantMainMiddleware has already run.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # TenantMainMiddleware sets request.tenant
        current_tenant = getattr(request, 'tenant', None)

        if request.user.is_authenticated and not getattr(request.user, 'is_superadmin', False):
            # Collect tenant IDs the user belongs to
            user_tenants = getattr(
                request.user, 'tenantuserrole_set', None
            )
            if user_tenants is not None:
                tenant_ids = user_tenants.values_list('tenant_id', flat=True)
                if current_tenant and current_tenant.id not in tenant_ids:
                    from django.http import HttpResponseForbidden
                    return HttpResponseForbidden("Access denied: not part of this tenant")

        response = self.get_response(request)
        return response
