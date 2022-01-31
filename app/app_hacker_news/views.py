from django.shortcuts import render
from django.http import HttpResponse
from .logic import HackerNews, DatabaseObjects, MODEL_LIST
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    if request.method == "POST":
        cat_name = request.POST.get("category_name")
        news = HackerNews()
        db_obj = DatabaseObjects()
        cat_model = None

        if cat_name in news.default_cat:
            cat_model = MODEL_LIST[news.default_cat.index(cat_name)]
            db_obj.object_set_model(cat_model)
        else:
            HttpResponse(f"<h2>Category name {cat_name} do not exist</h2>")

        if cat_model is not None:
            for item in news.get_news(cat_name):
                try:
                    db_obj.object_get(item)
                except ObjectDoesNotExist:
                    db_obj.object_create(item)
        else:
            HttpResponse(f"<h2>Model corrupted</h2>")

        return render(request, 'app_hacker_news/admin.html')
    else:
        return render(request, 'app_hacker_news/home.html')
