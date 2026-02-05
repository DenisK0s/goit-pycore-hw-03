from datetime import datetime

def get_days_from_today(date: str) -> int:
    current_dete = datetime.today()
    given_date = datetime.strptime(date, "%Y-%m-%d")
    
    delta = current_dete - given_date

    return delta.days
