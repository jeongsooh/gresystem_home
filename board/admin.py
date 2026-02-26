from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)
    
    # 관리자가 목록에서 노출 여부를 빠르게 변경할 수 있도록 설정
    list_editable = ('is_active',)
