def date_to_string_rus(d: 'datetime.date') -> str:
    """
    Returns text representation for a date of the standart datetime module.

    Language for month representation: Russian.

    Example:
    d = date(year=2020, month=5, day=15)
    return value: '15 мая 2020'
    """
    MONTHS = {
        1:  'января',
        2:  'февраля',
        3:  'марта',
        4:  'апреля',
        5:  'мая',
        6:  'июня',
        7:  'июля',
        8:  'августа',
        9:  'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }

    return str(d.day) + ' ' + MONTHS[d.month] + ' ' + str(d.year)


if __name__ == '__main__':
    from datetime import date, time
    d = date(year=2020, month=5, day=15)
    print(date_to_string_rus(d))
