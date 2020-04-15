# Letter Changes
# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Examples
# Input: "hello*3"
# Output: Ifmmp*3
# Input: "fun times!"
# Output: gvO Ujnft!

def LetterChanges(str):
    result = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in str:
        if char in letters:
            if char == letters[-1]:
                char = letters[0]
            else:
                idx = letters.find(char)
                char = letters[idx+1]
            result += char
        else:
            result += char
            continue
    list_result = list(result)
    for i in range(len(list_result)):
        if list_result[i] in 'aeiou':
            list_result[i] = list_result[i].upper()
    result = ''.join(list_result)
    return result

# keep this function call here 
print(LetterChanges("hello*3"))
print(LetterChanges("fun times!"))
print(LetterChanges("Argument goes here"))
print(LetterChanges("hello*3"))