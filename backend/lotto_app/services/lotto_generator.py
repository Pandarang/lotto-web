import random


def generate_lotto_numbers(count: int = 6, min_num: int = 1, max_num: int = 45) -> list[int]:
    """
    로또 번호 자동 생성 함수
    - 중복 없이 count개만큼 뽑아서
    - 정렬된 리스트로 반환한다.
    """
    # range(min_num, max_num + 1) 범위에서 중복 없이 count개 랜덤 추출
    numbers = random.sample(range(min_num, max_num + 1), count)
    numbers.sort()
    return numbers


def numbers_to_string(numbers: list[int]) -> str:
    """
    [1, 5, 12, 23, 32, 41]  ->  "1,5,12,23,32,41"
    형태로 변환해 주는 헬퍼 함수
    """
    return ",".join(str(n) for n in numbers)
