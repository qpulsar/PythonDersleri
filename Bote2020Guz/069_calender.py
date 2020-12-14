import calendar

takvim = calendar.TextCalendar(calendar.MONDAY)
metin = takvim.formatmonth(2020, 12)
print(metin)

web_takvim = calendar.HTMLCalendar()
mtn = web_takvim.formatmonth(220, 12)
print(mtn)
