from . models import Category
#for saving links
def Menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

