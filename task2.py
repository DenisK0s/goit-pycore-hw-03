import random

def get_numbers_ticket(min: int, max:int, quantity: int) -> list[int]:
    lower_bound = 1
    upper_bound = 100
    nums_range_list = list(range (min, max + 1))
    is_quantity_in_range = quantity <= len(nums_range_list)

    if min < lower_bound or max > upper_bound or not is_quantity_in_range:
        return []
    
    unique_random_numbers = random.sample(nums_range_list, quantity)
    sorted_unique_random_numbers = sorted(unique_random_numbers)
    
    return sorted_unique_random_numbers