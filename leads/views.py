from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LeadForm

def contact_view(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '상담 문의가 성공적으로 접수되었습니다. 담당자가 곧 연락드리겠습니다.')
            return redirect('core:home')
    else:
        form = LeadForm()
    
    return render(request, 'leads/contact.html', {'form': form})
