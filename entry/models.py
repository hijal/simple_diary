from django.db import models


class Entry(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
         verbose_name_plural = 'Entries'

