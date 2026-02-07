from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def get_days_from_today(date: str) -> int:
    current_dete = datetime.today()
    given_date = datetime.strptime(date, DATE_FORMAT)
    
    delta = current_dete - given_date

    return delta.days
