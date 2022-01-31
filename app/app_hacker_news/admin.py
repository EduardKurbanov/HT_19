from django.contrib import admin
from app_hacker_news.models import Askstories, Showstories, Newstories, Jobstories

admin.site.register(Askstories)
admin.site.register(Showstories)
admin.site.register(Newstories)
admin.site.register(Jobstories)
