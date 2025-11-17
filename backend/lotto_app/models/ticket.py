from django.db import models
from .draw import Draw

class Ticket(models.Model):
    # 어떤 회차에 대한 티켓인지
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, related_name='tickets')

    # 구매자 이름
    buyer_name = models.CharField(max_length=50)

    # 자동/수동 여부
    is_auto = models.BooleanField(default=False)

    # 선택된 번호 6개 (예: "3,11,22,27,35,41")
    numbers = models.CharField(max_length=50)

    # 구매 시각
    created_at = models.DateTimeField(auto_now_add=True)

    # 티켓 가격
    price = models.PositiveIntegerField(default=1000)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.draw.round}회차 - {self.buyer_name} - {self.id}"

    def get_numbers_list(self):
        return [int(n) for n in self.numbers.split(',')]
