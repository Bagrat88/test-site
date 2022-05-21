from django.db import models
from django.urls import reverse


class News(models.Model):

    title = models.CharField(max_length=150, verbose_name='name')
    content = models.TextField(blank=True, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    uodateed_at = models.DateTimeField(auto_now=True, verbose_name='update')
    photo = models.ImageField(upload_to='photos/%d/m/y/', verbose_name='photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'a news'
        verbose_name_plural = 'a news'
        ordering = ['-created_at']



class Category(models.Model):
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='category name')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']