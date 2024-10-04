#--------a------

"""
def cube(num):
    return num**3;

# Test cases
num = int(input("Enter number: "))
print("The cube is " ,cube(num))
"""

#--------b------

"""
def factorial(num):
    result=1
    if(num==0):
        result=1
    elif(num>0):
        for i in range(1,num+1):
            result=result*i
    else:
        result=-1
    return "The input must not be negative"

# Test cases
num = int(input("Enter number: "))
print("Factorial:" ,factorial(num))
"""
#--------c------
"""
def findAlphabeticallyLastWord(sentence):
    words = sentence.split()
    last_word = ""
    for word in words:
        if word > last_word:
            last_word = word
    
    return last_word

# Test cases
sentence = input("Enter sentence: ")
result = findAlphabeticallyLastWord(sentence.lower())
print(result)
"""   
#--------d------
 
def count_pattern(pattern, lst):
    pattern_len = len(pattern)
    count = 0
   
    for i in range(len(lst) - pattern_len + 1):
        match = True
        for j in range(pattern_len):
            if lst[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1

    return count

# Test cases
print("Pattern Appears",count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')),"Times") 
#print("Pattern Appears",count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')),"Times") 
    
        
    
