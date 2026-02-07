from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

# функція має впоратися з неправильним форматом вхідних даних.
def get_days_from_today(date: str) -> int:
    try:
        current_date = datetime.today()
        given_date = datetime.strptime(date, DATE_FORMAT)
        
        delta = current_date - given_date
        return delta.days
    except ValueError:
        # Handle invalid date format
        raise ValueError(f"Date must be in {DATE_FORMAT} format")
