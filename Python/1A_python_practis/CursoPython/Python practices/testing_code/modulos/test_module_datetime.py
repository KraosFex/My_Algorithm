from datetime import datetime, timedelta, date

before_week = datetime.now() - timedelta(7)

init_weekday = before_week - \
    timedelta(before_week.weekday(), hours=before_week.hour)

end_weekday = before_week + \
    timedelta(5 - before_week.weekday(),
              hours=(23 - before_week.hour))

print(before_week)
print(init_weekday)
print(end_weekday)
