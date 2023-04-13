from django.shortcuts import render  # noqa
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from accounts.models import Profile, Experience, Education


@require_GET
def home(request, slug):
    user = get_object_or_404(Profile, user_url=slug)
    experiences = Experience.objects.filter(profile=user)
    educations = Education.objects.filter(profile=user)

    context = {
        'user': user,
        'experiences': experiences,
        'educations': educations
    }
    return render(request, 'main.html', context)
