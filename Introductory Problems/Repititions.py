dna = input()

cur_character = None
cur_count = 0
max_count = 0

for character in dna:
    if character == cur_character:
        cur_count +=1
    else:
        cur_character = character
        cur_count = 1
    max_count = max(cur_count,max_count)

print(max_count)