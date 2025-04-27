from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('파인트', '파인트'),
    ('바',     '바'),
    ('컵',     '컵'),
    ('한정판', '한정판'),
]

class MainContent(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='static/products/', blank=True, null=True)
    pub_date    = models.DateTimeField(auto_now_add=True)
    category     = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='파인트')
    sales_count  = models.PositiveIntegerField(default=0)  # 인기 계산용

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '제품'
        verbose_name_plural = '제품들'

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
