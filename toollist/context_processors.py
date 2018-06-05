

def is_admin(request):
    if request.path.startswith('/admin/'):
        return {'navigation_admin': True}
    return {}
