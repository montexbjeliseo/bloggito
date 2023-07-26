from apps.posts.models import Category

def blog_context(request):
    data = {
        'app_name': 'Bloggito',
        'categories': Category.objects.all()
    }
    return data