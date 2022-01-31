from django.db import models


class Askstories(models.Model):
    by = models.TextField(default=None, null=True)
    id_news = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    type = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.id_news)


class Showstories(models.Model):
    by = models.TextField(default=None, null=True)
    id_news = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    type = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.id_news)


class Newstories(models.Model):
    by = models.TextField(default=None, null=True)
    id_news = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    type = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.id_news)


class Jobstories(models.Model):
    by = models.TextField(default=None, null=True)
    id_news = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    type = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.id_news)
