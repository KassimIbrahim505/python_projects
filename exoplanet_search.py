def has_exoplanet(readings):
    values = [int(char, 36) for char in readings]

    total = sum(values)
    count = len(values)

    for value in values:
        if value * 5 * count <= 4 * total:
            return True
    return False

print(has_exoplanet("freecodecamp"))


    #return readings