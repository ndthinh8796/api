from django.db import models


class WebURL(models.Model):
    url = CharField(max_length=100)

    def __str__(self):
        return self.url


class Conversation(models.Model):
    url = models.ForeignKey(WebURL, on_delete=models.CASCADE)
    params = models.CharField(max_length=250)

    def __str__(self):
        return '{}: {}'.format(self.url, self.params)
