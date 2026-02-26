from django.shortcuts import render, get_object_or_404
from .models import Notice

def notice_list(request):
    notices = Notice.objects.filter(is_active=True)
    return render(request, 'board/notice_list.html', {'notices': notices})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk, is_active=True)
    return render(request, 'board/notice_detail.html', {'notice': notice})
