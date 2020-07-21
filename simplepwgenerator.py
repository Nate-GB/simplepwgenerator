
import random

def shuffle(string):
    """Shuffles all the characters of a string"""
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #random uppercase character 1
uppercaseLetter2=chr(random.randint(65,90)) #random uppercase character 2
lowercaseLetter1=chr(random.randint(97,122)) #random lowercase character 1
lowercaseLetter2=chr(random.randint(97,122)) #random lowercase character 2
digit1=chr(random.randint(48,57)) #random digit 1
digit2=chr(random.randint(48,57)) #random digit 2
punctuationSign1=chr(random.randint(33,47)) #random punctuation character 1
punctuationSign2=chr(random.randint(58,64)) #random punctuation character 2

#Generate password using all the characters and then randomize them
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

#Output
print(password)
