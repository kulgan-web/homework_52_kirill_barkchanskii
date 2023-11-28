from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.CharField(max_length=150, null=False, blank=False, verbose_name='Описание задачи')
    date_of_completion = models.DateField(null=True, blank=True, verbose_name='Дата выполнения, вводить в формате YYYY-mm-dd')
    status = models.TextField(max_length=50, default='new', verbose_name='Статус задачи', choices=status_choices)


    def __str__(self):
        return f'{self.id} {self.description}'

