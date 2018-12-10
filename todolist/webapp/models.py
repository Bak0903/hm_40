from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Задача')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, null=True, blank=True, default='Не выполнен', verbose_name='Статус')
    created_at = models.DateField(verbose_name="Дата создания")

    def __str__(self):
        return self.name
