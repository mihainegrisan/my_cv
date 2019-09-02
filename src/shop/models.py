from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name = 'products',
                                 on_delete = models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    # Always use a DecimalField instead of FloatField for monetary values to avoid float rounding errors
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    # auto_now_add - updates the value with the time and date of creation of record.
    created = models.DateTimeField(auto_now_add=True)
    # auto_now - updates the value of field to current time and date every time the Model.save() is called.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        # Index together to query products by both id and slug. Both fields are indexed together to improve performances for queries that utilize the two fields.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
