import webbrowser
from datetime import date, timedelta, datetime

today = date.today()
interval = timedelta(days=30)

end = today - interval
end = datetime.combine(end, datetime.min.time())
url = f"https://mail.proton.me/u/0/trash#end={int(end.timestamp())}"
webbrowser.open(url)

url = "https://drive.proton.me/u/0/trash"
webbrowser.open(url)
