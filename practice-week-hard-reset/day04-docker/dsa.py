input = [100, 200, 1, 3, 2, 34, 12]
count = 0 
longest_streak = 0
current_num = 0
current_streak = 1
input_set = set(input)

for n in input_set:
    if n-1 not in input_set:
        current_num = n
        current_streak = 1

        while current_num + 1 in input_set:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

print(f"Longest streak was: {longest_streak}")
