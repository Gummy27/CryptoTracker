from datetime import date, datetime

def getDate():
    return str(date.today())+"-"+str(datetime.now().hour)