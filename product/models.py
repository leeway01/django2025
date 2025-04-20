from django.db import models

class MainContent(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='static/products/', blank=True, null=True)
    pub_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '제품'
        verbose_name_plural = '제품들'

    def __str__(self):
        return self.title
