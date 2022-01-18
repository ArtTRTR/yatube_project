from django.http import HttpResponse


def index(request):
    return HttpResponse('You <i>can\'t </i> receive correct <b>responce</b>,<br> '
                        'if you don\'t have correct <s>questions</s>.')


def group_posts(request, slug):
    return HttpResponse('Posts here')
