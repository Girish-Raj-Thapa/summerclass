from . models import Page 

def pages_links(request):
    pages = Page.objects.filter(active=True)
    return {'pages':pages}