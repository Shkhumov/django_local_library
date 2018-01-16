from django.db import models

# Create your models here.


class Callback(models.Model):
    call_name = models.CharField(max_length=20)
    call_phone = models.CharField(verbose_name='Тел.', max_length=15 , blank=True)

    class Meta:
        verbose_name = 'Зворотній виклик'
        db_table = 'callback'

    def __str__(self):
        return self.call_name