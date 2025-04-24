from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse

from accounts.models import Profile


def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        return HttpResponse(status=400)

    with transaction.atomic():
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(
            user=user,
            nickname=request.POST.get('nickname'),
            bio=request.POST.get('bio'),
            location=request.POST.get('location'),
            weight=request.POST.get('weight'),
            website=request.POST.get('website'),
        )

    return HttpResponse(status=201)
