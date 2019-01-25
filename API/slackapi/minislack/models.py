from django.db import models


# class Channel(models.Model):
#     channel_name = CharField(max_length=25)
#
#     def __str__(self):
#         return self.channel_name


class Conversation(models.Model):
    # channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    def __str__(self):
        return '{}: {}'.format(self.user, self.text)
