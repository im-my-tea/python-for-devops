groups = {}

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

for word in input:
    sorted_word = "".join(sorted(word))
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]

print(list(groups.values()))