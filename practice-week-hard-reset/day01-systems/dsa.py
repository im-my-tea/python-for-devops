def is_valid(s):
    # Map closer -> opener
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c in pairs:
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False

print(is_valid("({[]})"))


def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for p in prices:
        if p < min_price:
            min_price = p
        elif (p - min_price) > profit:
            profit = p - min_price

    return profit

print(max_profit([7, 1, 5, 3, 6, 4]))