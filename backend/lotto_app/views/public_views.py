from django.shortcuts import render, get_object_or_404, redirect
from lotto_app.models import Draw, Ticket
from lotto_app.forms.ticket_form import TicketPurchaseForm
from lotto_app.services.lotto_checker import get_rank

def home(request):
    # ìµœì‹  ?šŒì°? ?‘œ?‹œ
    latest_draw = Draw.objects.order_by('-round').first()
    return render(request, 'lotto_app/home.html', {'latest_draw': latest_draw})

def buy_ticket(request):
    # êµ¬ë§¤ ê°??Š¥?•œ ?šŒì°? ì°¾ê¸°
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
    # ?‹°ì¼? ?ƒ?„¸ + ?“±?ˆ˜ ê³„ì‚°
    ticket = get_object_or_404(Ticket, id=ticket_id)
    rank = get_rank(ticket.draw, ticket)
    return render(request, 'lotto_app/ticket_detail.html', {'ticket': ticket, 'rank': rank})

def check_result(request):
    # ?‹°ì¼? IDë¡? ?‹¹ì²? ì¡°íšŒ
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
