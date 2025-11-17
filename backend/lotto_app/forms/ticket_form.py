from django import forms
from lotto_app.service.lotto_generator import generate_lotto_numbers, numbers_to_string

class TicketPurchaseForm(forms.Form):
    # 이름
    buyer_name = forms.CharField(max_length=50)

    # 수동/자동 선택
    MODE_CHOICES = (
        ('manual', '수동'),
        ('auto', '자동'),
    )
    mode = forms.ChoiceField(choices=MODE_CHOICES, widget=forms.RadioSelect)

    # 수동 번호 입력 (6개)
    n1 = forms.IntegerField(min_value=1, max_value=45, required=False)
    n2 = forms.IntegerField(min_value=1, max_value=45, required=False)
    n3 = forms.IntegerField(min_value=1, max_value=45, required=False)
    n4 = forms.IntegerField(min_value=1, max_value=45, required=False)
    n5 = forms.IntegerField(min_value=1, max_value=45, required=False)
    n6 = forms.IntegerField(min_value=1, max_value=45, required=False)

    def clean(self):
        # 수동일 때 번호 6개 검증
        cleaned = super().clean()
        if cleaned.get('mode') == 'auto':
            return cleaned

        nums = [cleaned.get(f'n{i}') for i in range(1, 7)]
        if any(n is None for n in nums):
            raise forms.ValidationError("번호 6개를 모두 입력하세요.")
        if len(set(nums)) != 6:
            raise forms.ValidationError("중복 없는 번호를 입력하세요.")
        return cleaned

    def get_numbers_string(self):
        # 자동/수동에 따라 번호 문자열 생성
        if self.cleaned_data['mode'] == 'auto':
            nums = generate_lotto_numbers()
        else:
            nums = [self.cleaned_data[f'n{i}'] for i in range(1, 7)]
            nums.sort()
        return numbers_to_string(nums)
