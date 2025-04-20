# orders/models.py
from django.db import models
from django.conf import settings
from product.models import MainContent  # MainContent를 상품 모델로 사용

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', '결제 완료'),
        ('D', '배송 중'),
        ('S', '발송 완료'),
        ('C', '주문 취소'),
    ]

    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    tracking_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '주문'
        verbose_name_plural = '주문들'

    def __str__(self):
        return f"주문#{self.pk} – {self.user.username}"

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product  = models.ForeignKey(MainContent, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = '주문 상품'
        verbose_name_plural = '주문 상품들'

    def __str__(self):
        return f"{self.product.title} x{self.quantity}"
