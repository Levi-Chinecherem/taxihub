from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            # Redirect to a page indicating they don't have permission
            return redirect('no_permission')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
