from collections import deque


def find_cheapest_price(n, flights, src, dst, k):
    adjacency_list = {city: [] for city in range(n)}

    for from_i, to_i, price in flights:
        adjacency_list[from_i].append((to_i, price))

    cheapest_price = float('inf')

    # (stop, price)
    queue = deque([(src, 0)])

    cities_left = k + 2

    while queue and cities_left > 0:
        for _ in range(len(queue)):
            city, price = queue.popleft()

            if city == dst:
                cheapest_price = min(cheapest_price, price)

            for neighbor, price_to_neighbor in adjacency_list[city]:
                queue.append((neighbor, price + price_to_neighbor))

        cities_left -= 1

    return cheapest_price if cheapest_price != float('inf') else -1


print(
    find_cheapest_price(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0, 3, 1))
