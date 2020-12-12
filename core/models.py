from django.db import models
from django.urls import reverse

class Todo(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=500, verbose_name='описание')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')
    close_date = models.DateTimeField(null=True, blank=True, verbose_name='время закрытия')

    def get_absolute_url(self):
        return reverse('core:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'
