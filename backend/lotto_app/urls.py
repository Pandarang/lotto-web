from django.urls import path
from lotto_app.views import public_views

# 앱 네임스페이스
app_name = 'lotto_app'

# 로또 앱 URL 매핑
urlpatterns = [
    path('', public_views.home, name='home'),                       # 메인 화면
    path('buy/', public_views.buy_ticket, name='buy_ticket'),       # 로또 구매
    path('ticket/<int:ticket_id>/', public_views.ticket_detail, name='ticket_detail'),  # 티켓 상세
    path('check/', public_views.check_result, name='check_result'), # 티켓 ID로 당첨 조회
]
