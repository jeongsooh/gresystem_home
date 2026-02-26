from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'address', 'product_interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름을 입력해주세요'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '연락처 (예: 010-1234-5678)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '설치 예정 주소 (시/군/구까지)'}),
            'product_interest': forms.Select(choices=[
                ('', '관심 제품 선택'),
                ('CP700P', 'CP700P (7kW 고급형)'),
                ('CP700', 'CP700 (7kW 스탠다드)'),
                ('CP100', 'CP100 (3.5kW 콘센트형)'),
                ('Etc', '기타 / 잘 모름')
            ], attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '궁금하신 점이나 특별한 설치 환경(단독주택, 비가림막 필요 등)을 적어주세요.'}),
        }
