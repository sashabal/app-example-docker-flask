from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def whoami(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "authenticated": True,
            "username": request.user.username,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
            "user_id": request.user.pk,
        })
    return JsonResponse({"authenticated": False})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('whoami/', whoami),
]
