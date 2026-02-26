from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    is_active = models.BooleanField(default=True, verbose_name="노출 여부")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항 목록'
        ordering = ['-created_at']
