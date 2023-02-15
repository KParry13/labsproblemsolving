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
    # words_capitalized = ''
    for index in range(0, cap_word):
        print(string[index])
    
        if string[index-1] == ' ' :
            print(string[index].upper())
        elif string[index +1] == '':
            print (string[index].lower())
    #   else:
    #       print (string[index].lower())
        


capitalize_words('you got this!')