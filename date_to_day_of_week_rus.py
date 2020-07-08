def date_to_day_of_week_rus(d: 'datetime.date') -> str:
    """
    Returns name of a weekday for a date of the standart datetime module.

    Language: Russian.

    Example:
    d = date(year=2020, month=5, day=15)
    return value: 'пятница'
    """
    WEEKDAY = {
        0:  'понедельник',
        1:  'вторник',
        2:  'среда',
        3:  'четверг',
        4:  'пятница',
        5:  'суббота',
        6:  'воскресенье'
    }

    return WEEKDAY[d.weekday()]


if __name__ == '__main__':
    from datetime import date, time
    d = date(year=2020, month=5, day=15)
    print(date_to_day_of_week_rus(d))
