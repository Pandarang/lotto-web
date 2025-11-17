from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # 관리자 페이지
    path('', include('lotto_app.urls')),   # 로또 앱 URL 포함
]
