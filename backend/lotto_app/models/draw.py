from django.db import models
from django.utils import timezone

class Draw(models.Model):
    # 로또 회차 번호 (1회, 2회, 3회…)
    round = models.PositiveIntegerField(unique=True)

    # 추첨 날짜
    draw_date = models.DateField(default=timezone.now)

    # 당첨 번호 6개 + 보너스 번호
    n1 = models.PositiveIntegerField()
    n2 = models.PositiveIntegerField()
    n3 = models.PositiveIntegerField()
    n4 = models.PositiveIntegerField()
    n5 = models.PositiveIntegerField()
    n6 = models.PositiveIntegerField()
    bonus = models.PositiveIntegerField()

    # 티켓 구매 가능 여부
    is_open = models.BooleanField(default=True)

    class Meta:
        ordering = ['-round']

    def __str__(self):
        return f"{self.round}회차"
