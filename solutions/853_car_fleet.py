# sort fleets based on position from closest to target to furthest
# loop through each position and speed, push time to target onto a stack
# if current time is less than or equal to previous time, it means the current car combines with previous car, pop the current car
def car_fleet(target, position, speed):
    cars = [(p, s) for p, s in zip(position, speed)]
    cars.sort(key=lambda car: car[0], reverse=True)

    fleets = []

    for p, s in cars:
        fleets.append((target - p) / s)

        if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
            fleets.pop()

    return len(fleets)