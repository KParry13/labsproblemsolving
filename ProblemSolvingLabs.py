# reverse the string so it is spelled out backwards

def reversed_string(string):
    final_index = len(string)-1
    string_reversed = ''
    for index in range(final_index,-1,-1):
        string_reversed += string[index]
    print (string_reversed)
        

# reversed_string('Hello World')


# Capitalize the first letter of each word in a string.

def capitalize_words(string):
    cap_word = len(string)
    
    for index in range(0, cap_word):
       
    
        if string[index] == string[(0)]:
            print(string[index].upper())
        elif string[index-1] == ' ' :
            print(string[index].upper())
        else:
            print (string[index].lower())
        


# capitalize_words('you got this!')



# Palindrome
# User input
# Check to see if the word is a palindrone
# Check to see if the word is NOT a palindrone

def palindrone_checker():
    user_word = input("Please enter a word to check if it is a palindrone: ").lower()
    print (user_word)
    reverse_user_word = reversed_string(user_word)
    print (f"Your word is: {user_word}")
    print (f"The reverse is {reverse_user_word}")
    if user_word == reverse_user_word:
        print ("This is a palindrone!")
    else:
        print ("This is not a palindrone.")

# palindrone_checker()
#


# user input
# compress amount of same characters to make string shorter
'''compress kkkkaayyyylllllllllaaaa down to 4k2a4y9l4a 
need to select the first charater from input string
# index
add it to the compressed string
# compressed = '' (a new string all together)
count the number of same charaters in a row in the string and add the count if it is more than 1 only

pick the next character and repeat the steps above until the end of the string
# return
'''

def compressing_a_string(string):
    index = 0
    compressed = ''
    len_str = len(string)
    while index 



# compressing_a_string('kkkkaayyyylllllllllaaaa')


# Happy Numbers


# Prime Numbers

