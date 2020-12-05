from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('offers:offer_list_by_category',
                       args=[self.slug])


class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbode_name_plural = 'categories'


def __str__(self):
    return self.name


class Offers(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    adres = models.CharField(max_length=300, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    bonus = models.FloatField(max_length=3, db_index=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('offers:offer_detail',
                       args=[self.id, self.slug])


class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'),)


def __str__(self):
    return self.name
