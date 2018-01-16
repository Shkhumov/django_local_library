from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



# Create your models here.


class Article(models.Model):
    class Meta:
        db_table = "article"
        verbose_name = 'Колонка1'

    article_title = models.CharField(max_length=200)
    article_author = models.ForeignKey(User)
    article_content = models.TextField()

    def __str__(self):
        return self.article_title

class Article_two(models.Model):
    class Meta:
        db_table = "article2"
        verbose_name = 'Колонка2'

    article2_title = models.CharField(max_length=200)
    article2_author = models.ForeignKey(User)
    article2_content = models.TextField()

    def __str__(self):
        return self.article2_title


class Contact(models.Model):
    class Mata:
        db_table = "contact"
        verbose_name = 'Контакти'

    contact_title = models.CharField(verbose_name='Заголовок' ,max_length=200)
    contact_author = models.ForeignKey(User)
    contact_emeil = models.EmailField(verbose_name='Email',max_length=50, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    website = models.URLField(verbose_name='Facebook',null=True, blank=True)

    def __str__(self):
        return self.contact_title


class Posts(models.Model):
    class Meta:
        db_table = "posts"
        verbose_name = 'Популярны стилі в дизайні'

    post_title = models.CharField(max_length=20, verbose_name= 'Заголовок')
    post_content = models.TextField(max_length=512, verbose_name='Жатий контент')
    post_img = models.ImageField(upload_to = 'home/img')

    def __str__(self):
        return self.post_title


class Reclama(models.Model):
    class Meta:
        db_table = "reclama"
        verbose_name = "Реклама"

    reclama_title =  models.CharField(max_length=50, verbose_name='Заголовок')
    reclama_content = models.TextField(max_length=200, verbose_name='Стаття')

    def __str__(self):
        return self.reclama_title







