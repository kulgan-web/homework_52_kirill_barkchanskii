from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=150, null=False, blank=False, verbose_name='Описание задачи')
    status = models.CharField(max_length=50, default='new', verbose_name='Статус задачи')
    date_of_completion = models.TextField(null=True, verbose_name='Дата выполнения YYYY-mm-dd')

    def __str__(self):
        return f'{self.id} {self.description}'

