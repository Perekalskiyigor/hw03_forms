from datetime import date


def year(request):
    if request == "request":
        today = date.today()
        return {"year": today.year}
