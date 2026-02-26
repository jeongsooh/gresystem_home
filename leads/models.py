from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = (
        ('new', '신규 문의'),
        ('contacted', '연락 완료'),
        ('closed', '종료'),
    )

    name = models.CharField(max_length=50, verbose_name="고객명")
    phone = models.CharField(max_length=20, verbose_name="연락처")
    address = models.CharField(max_length=200, verbose_name="설치 지역", help_text="예: 서울시 강남구, 경기도 수원시")
    product_interest = models.CharField(max_length=50, blank=True, null=True, verbose_name="관심 제품군")
    message = models.TextField(blank=True, null=True, verbose_name="상담 내용")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="응대 상태")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="문의 접수일")

    def __str__(self):
        return f"[{self.get_status_display()}] {self.name} - {self.address}"

    class Meta:
        verbose_name = '설치 상담 문의 (리드)'
        verbose_name_plural = '설치 상담 리스트'
        ordering = ['-created_at']
