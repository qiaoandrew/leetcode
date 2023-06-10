def least_consecutive_cards_to_match(cards):
    least = float('inf')
    count = {}
    left = 0
    for right in range(len(cards)):
        count[cards[right]] = count.get(cards[right], 0) + 1
        while count[cards[right]] > 1:
            least = min(least, right - left + 1)
            count[cards[left]] -= 1
            left += 1
    return least if least != float('inf') else -1
