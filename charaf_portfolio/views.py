from django.shortcuts import render
from account.models import Image, Information, InstagramFeed


def homePage(request):
    template_name = 'homePage.html'
    images = Image.objects.all().order_by('-id')
    info = Information.objects.first()
    feeds = InstagramFeed.objects.all().order_by('-id')
    context = {
        'images': images,
        'info': info,
        'feeds': feeds
    }
    return render(request, template_name, context)