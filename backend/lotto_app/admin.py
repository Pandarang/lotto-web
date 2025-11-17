from django.contrib import admin
from lotto_app.models import Draw, Ticket

# 관리자 페이지에 Draw 등록
@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display = ('round', 'draw_date', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'bonus', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('round',)

# 관리자 페이지에 Ticket 등록
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer_name', 'draw', 'is_auto', 'numbers', 'created_at')
    list_filter = ('is_auto', 'draw')
    search_fields = ('buyer_name', 'numbers')
