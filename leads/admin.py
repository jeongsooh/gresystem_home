from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'product_interest', 'status', 'created_at')
    list_filter = ('status', 'product_interest', 'created_at')
    search_fields = ('name', 'phone', 'address', 'message')
    readonly_fields = ('created_at',)
    
    # 관리자가 목록에서 지원 상태를 빠르게 변경할 수 있도록 설정
    list_editable = ('status', 'product_interest')
