from datetime import date

def moon_phase(date_string):
    reference = date(2000, 1, 6)
    given = date.fromisoformat(date_string)

    days_passed = (given - reference).days
    day_of_cycle = days_passed % 28 + 1

    if day_of_cycle <= 7:
        return "New"
    if day_of_cycle <= 14:
        return "Waxing"
    if day_of_cycle <= 21:
        return "Full"
    return "Waning"

    return date_string

print(moon_phase('2000-01-14'))