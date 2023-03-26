from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')
    close = models.BooleanField(default=False, verbose_name='Выполнение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
