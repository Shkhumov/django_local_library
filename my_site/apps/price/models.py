from django.db import models

# Create your models here.


class Price(models.Model):
    price_title = models.CharField(verbose_name= 'Заголовок',max_length= 50)
    price_text = models.TextField(blank=True)
    number = models.IntegerField(null=True, blank=True)
    threshold = models.IntegerField(null=True, blank=True)
    threshold2 = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            self.threshold2 = self.threshold * self.number
        except TypeError:
            pass
        super(Price, self).save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        db_table = 'price'
        verbose_name = 'Прайс лист(ціна)'

    def __str__(self):
        return '%s' % self.price_title