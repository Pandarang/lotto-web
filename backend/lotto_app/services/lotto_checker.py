from lotto_app.models import Draw, Ticket

#Ticket 객체에 저장된 문자열 번호를 {1, 5, 12, 23, 32, 41} 같은 집합으로 변환
def get_ticket_numbers_set(ticket: Ticket) -> set[int]:
    return set(ticket.get_numbers_list())

# Draw 객체의 당첨 번호 6개를 집합으로 변환(보너스 번호는 제외)
def get_draw_numbers_set(draw: Draw) -> set[int]:
    return {draw.n1, draw.n2, draw.n3, draw.n4, draw.n5, draw.n6}

# 당첨 번호 6개와 티켓 번호의 일치 개수를 반환
def count_matches(draw: Draw, ticket: Ticket) -> int:
    win_set = get_draw_numbers_set(draw)
    ticket_set = get_ticket_numbers_set(ticket)
    return len(win_set & ticket_set)  # 교집합 개수

#보너스 번호가 티켓 번호 안에 포함되어 있는지 여부
def is_bonus_matched(draw: Draw, ticket: Ticket) -> bool:
    return draw.bonus in ticket.get_numbers_list()


def get_rank(draw: Draw, ticket: Ticket) -> int | None:

    match = count_matches(draw, ticket)
    bonus = is_bonus_matched(draw, ticket)

    if match == 6:
        return 1
    elif match == 5 and bonus:
        return 2
    elif match == 5:
        return 3
    elif match == 4:
        return 4
    elif match == 3:
        return 5
    else:
        return None