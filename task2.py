import random

LOWER_BOUND = 1
UPPER_BOUND = 100

def get_numbers_ticket(min: int, max:int, quantity: int) -> list[int]:
    nums_range_list = list(range (min, max + 1))
    is_quantity_in_range = quantity <= len(nums_range_list)

    if min < LOWER_BOUND or max > UPPER_BOUND or not is_quantity_in_range:
        return []
    
    unique_random_numbers = random.sample(nums_range_list, quantity)
    sorted_unique_random_numbers = sorted(unique_random_numbers)
    
    return sorted_unique_random_numbers