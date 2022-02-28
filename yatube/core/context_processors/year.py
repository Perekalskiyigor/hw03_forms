from datetime import date


def year(request):
    if request == "request":
        print
    """Добавляет переменную с текущим годом."""
    today = date.today()
    return {
        "year": today.year
    }
