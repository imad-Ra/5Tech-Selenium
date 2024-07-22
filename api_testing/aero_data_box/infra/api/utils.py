from datetime import datetime, timezone

def format_time_and_date_to_X(times, date):
    # Assuming times is in format "HH:MM" and date is in format "YYYY-MM-DD"
    datetime_obj = datetime.strptime(f"{date} {times}", "%Y-%m-%d %H:%M")
    datetime_utc = datetime_obj.replace(tzinfo=timezone.utc)
    return datetime_utc.strftime("%Y-%m-%d %H:%MZ")

def get_current_time_and_date_formatted():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")