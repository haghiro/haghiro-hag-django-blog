from .models import Category

def all_category(request):
    categoroy_list = Category.objects.all()

    params = {
        'category_list': categoroy_list,
    }

    return params
