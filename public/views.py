from django.shortcuts import render
from .tasks import confirm_celery_running

# Create your views here.
def home(request):
    confirm_celery_running.delay()
    return render(request, 'public/home.html')