from datetime import date, datetime, timedelta



def dates(x):
    now = datetime.now()
    one_week_ago = now-timedelta(days=x)
    return [now, one_week_ago]


def date_s(x, y):
    if y < 10:
            y = f'0{y}'
    x = str(x).split()[0]
    return datetime.fromisoformat(f'{x}T{y}:00:00')


def date_for_filter(x) -> list:
    m = x['mounth']
    y = x['year']
    d_1 = datetime(int(y), int(m), 1)
    d_2 = d_1 + timedelta(days=30)

    return [d_2, d_1]


def year(x):
    year = x.created_at.year
    now = date.today().year
    data = [year]
    while year != now:
        year += 1
        data.append(year)
    
    return data

    