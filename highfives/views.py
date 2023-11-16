from django.shortcuts import render
from .models import HighFive


def list_highfives(request):
    highfives = HighFive.objects.all()
    return render(
        request,
        'highfives/index.html',
        {'highfives': highfives}
    )
