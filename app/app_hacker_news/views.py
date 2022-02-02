from django.shortcuts import render
from django.http import HttpResponse
from .logic import HackerNews, DatabaseObjects, MODEL_LIST


# Create your views here.
def home(request):
    if request.method == "POST":
        cat_name = request.POST.get("category_name")
        db_obj = DatabaseObjects()
        news_obj = HackerNews()
        news_list = None
        cat_model = None
        available_obj_list: list = []

        if cat_name in news_obj.default_cat:
            cat_model = MODEL_LIST[news_obj.default_cat.index(cat_name)]
            db_obj.object_set_model(cat_model)

            for items in cat_model.objects.all():
                available_obj_list.append(items.id_news)

            news_list = news_obj.get_news(cat_name, available_obj_list)
        else:
            HttpResponse(f"<h2>Category name {cat_name} do not exist</h2>")

        if cat_model is not None:
            for item in news_list:
                db_obj.object_create(item)
        else:
            HttpResponse(f"<h2>Model corrupted</h2>")

        return render(request, 'app_hacker_news/admin.html')
    else:
        return render(request, 'app_hacker_news/home.html')
