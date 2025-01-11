from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Название')
    content = models.TextField(verbose_name = 'Описание')
    price = models.FloatField(verbose_name = 'Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name = 'Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    image = models.ImageField(upload_to='Bb_images/', null=True, blank=True, verbose_name=('Изображение'))

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric (models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']