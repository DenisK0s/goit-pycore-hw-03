from datetime import datetime, timedelta

MAX_DAYS = 7
WEEKEND = [5, 6]
DATE_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    current_date = datetime.today().date()
    max_date = current_date + timedelta(days=MAX_DAYS)

    upcoming_birthdays = []
    
    for user in users:
        user_bd_date = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        user_bd_this_year = user_bd_date.replace(year=current_date.year)
        user_bd_next_year = user_bd_date.replace(year=current_date.year + 1)
        is_user_bd_next_year = user_bd_this_year < current_date
        upcoming_user_bd = user_bd_next_year if is_user_bd_next_year else user_bd_this_year 

        is_user_bd_within_range = upcoming_user_bd >= current_date and upcoming_user_bd < max_date

        if is_user_bd_within_range:
            congratulation_date = upcoming_user_bd
            user_bd_weekday = upcoming_user_bd.weekday()
            is_user_bd_on_weekend = user_bd_weekday in WEEKEND

            if is_user_bd_on_weekend:
                additional_days_number = MAX_DAYS - user_bd_weekday
                next_monday = upcoming_user_bd + timedelta(days=additional_days_number)
                congratulation_date = next_monday

            congratulation_date_string = congratulation_date.strftime(DATE_FORMAT)
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date_string}
            )
    
    return upcoming_birthdays