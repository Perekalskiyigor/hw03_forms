import datetime

def year(request):
    d = datetime.date.today()
    d = d.year  
    return {
        'year': d 
    }