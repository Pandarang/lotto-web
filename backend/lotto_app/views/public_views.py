from django.shortcuts import render, get_object_or_404, redirect
from lotto_app.models import Draw, Ticket
from lotto_app.forms.ticket_form import TicketPurchaseForm
from lotto_app.service.lotto_checker import get_rank

def home(request):
    # 최신 회차 표시
    latest_draw = Draw.objects.order_by('-round').first()
    return render(request, 'lotto_app/home.html', {'latest_draw': latest_draw})

def buy_ticket(request):
    # 구매 가능한 회차 찾기
    draw = Draw.objects.filter(is_open=True).order_by('-round').first()

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            numbers = form.get_numbers_string()
            ticket = Ticket.objects.create(
                draw=draw,
                buyer_name=form.cleaned_data['buyer_name'],
                is_auto=(form.cleaned_data['mode'] == 'auto'),
                numbers=numbers
            )
            return redirect('lotto_app:ticket_detail', ticket.id)
    else:
        form = TicketPurchaseForm()

    return render(request, 'lotto_app/buy_ticket.html', {'draw': draw, 'form': form})

def ticket_detail(request, ticket_id):
    # 티켓 상세 + 등수 계산
    ticket = get_object_or_404(Ticket, id=ticket_id)
    rank = get_rank(ticket.draw, ticket)
    return render(request, 'lotto_app/ticket_detail.html', {'ticket': ticket, 'rank': rank})

def check_result(request):
    # 티켓 ID로 당첨 조회
    ticket = None
    rank = None
    ticket_id = request.GET.get('ticket_id')

    if ticket_id:
        try:
            ticket = Ticket.objects.get(id=ticket_id)
            rank = get_rank(ticket.draw, ticket)
        except Ticket.DoesNotExist:
            ticket = None

    return render(request, 'lotto_app/check_result.html', {'ticket': ticket, 'rank': rank})
