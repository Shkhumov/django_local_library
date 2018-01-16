from django.db import models

# Create your models here.

class About(models.Model):

    about_title = models.CharField(max_length=50, blank=True,verbose_name='Заголовок')
    about_test = models.TextField(max_length=1000, blank=True, verbose_name='Стаття')
    about_img = models.ImageField(upload_to='home/img', blank=True)

    class Meta:
        db_table = 'about'
        verbose_name = ('Про тебе')

    def __str__(self):
        return self.about_title





