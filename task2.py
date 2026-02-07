import random

LOWER_BOUND = 1
UPPER_BOUND = 1000

def get_numbers_ticket(min: int, max:int, quantity: int) -> list[int]:

    if min < LOWER_BOUND or max > UPPER_BOUND:
        return []
    
    nums_range_list = list(range(min, max + 1))
    is_quantity_in_range = quantity <= len(nums_range_list)

    if is_quantity_in_range:
        unique_random_numbers = random.sample(nums_range_list, quantity)
        return sorted(unique_random_numbers)
    else:
        return []