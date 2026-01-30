s = input().split()
s_reversed = []
final_list = []
final_txt = ''

# Reverse order of words
s_reversed = s[::-1]

for i in range(len(s_reversed)):
    # Begins with a consonant or a vowel?
    if s_reversed[i].startswith('a') == True or s_reversed[i].startswith('e') == True or s_reversed[i].startswith('i') == True or s_reversed[i].startswith('o') == True or s_reversed[i].startswith('u') == True:
        final_list.append(s_reversed[i])
    else:
        # Has an even or odd number of characters?
        if len(s_reversed[i]) % 2 == 0:
            final_list.append(s_reversed[i])
        else:
            # Reverse characters of the word
            word_reversed = s_reversed[i][::-1]
            final_list.append(word_reversed)

# Remove duplicates
final_list = list(dict.fromkeys(final_list))

# Converting from the list to the final string
for x in range(len(final_list)):
    if x == len(final_list) - 1:
        final_txt += final_list[x]
    else:
        final_txt += final_list[x] + ' '
            
print(final_txt)
