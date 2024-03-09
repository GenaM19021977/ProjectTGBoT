from django.db import models

class Mebel(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField(max_digits=62, decimal_places=8)
    description = models.TextField(
        verbose_name='Описание с куфара'
    )
