from django.db import models

class Snake(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Полный текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/newinfo/{self.id}'
    class Meta:
        verbose_name = 'Змея'
        verbose_name_plural = 'Змейки'
