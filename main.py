from fastapi import FastAPI
from datetime import date

app = FastAPI(title="Days Before New Year API")

def days_until_new_year() -> int:
    """Рассчитывает количество дней до следующего 1 января."""
    today = date.today()
    # Определяем год следующего Нового года
    next_year = today.year + 1
    next_new_year = date(next_year, 1, 1)
    
    # Если сегодня 1 января, то до следующего Нового года ровно 365 или 366 дней
    if today.month == 1 and today.day == 1:
        delta = next_new_year - today
        return delta.days
    else:
        # Если ещё не 1 января текущего года, то Новый год в этом году
        current_new_year = date(today.year, 1, 1)
        if today > current_new_year:
            # Сегодня после 1 января, значит следующий Новый год в следующем календарном году
            delta = next_new_year - today
        else:
            # Сегодня до 1 января (но такого не может быть при проверке выше, оставим для полноты)
            delta = current_new_year - today
        return delta.days

@app.get("/info")
async def get_info():
    return {"days_before_new_year": days_until_new_year()}