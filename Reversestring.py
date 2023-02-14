'''
I want to reverse "Hello" so it will be spelled "olleH".
I need to write a loop that will reverse the string.
I need to write a loop that adds the letters together so it just spells "olleH".
'''

word = "Hello"
reversed_word = ''

for i in range(len(word)-1,-1,-1):
    reversed_word += word[i]
print(reversed_word)




