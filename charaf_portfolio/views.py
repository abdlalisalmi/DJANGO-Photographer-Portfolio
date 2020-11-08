from django.shortcuts import render
from account.models import Image, Information


def homePage(request):
    template_name = 'homePage.html'
    images = Image.objects.all().order_by('-id')
    info = Information.objects.first()
    context = {
        'images': images,
        'info': info,
    }
    return render(request, template_name, context)