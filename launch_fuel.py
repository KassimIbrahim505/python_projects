def launch_fuel(payload):
    fuel = payload/5

    while True:
        needed = (payload + fuel)/5
        additional = needed - fuel
        fuel = needed

        if additional < 1:
            break

    return round(fuel, 1)

print(launch_fuel(50))  # Example usage