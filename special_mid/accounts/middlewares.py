from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth import authenticate

class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.profile = None  

        if request.user.is_authenticated:
            request.profile, created = Profile.objects.get_or_create(user=request.user)

        elif request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                request.profile, created = Profile.objects.get_or_create(user=user)

        response = self.get_response(request)
        return response
