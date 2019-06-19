from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return '이름: {}, 주소: {}'.format(self.site_name, self.url)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])