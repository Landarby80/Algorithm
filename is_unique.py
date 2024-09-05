# Implement an algorithm to determine if a string has all unique characters.

def is_unique(word1):

    # empty list to check if they are unique
    check = []

    for letter in word1:
        if letter in check:
            return False
        else:
            check.append(letter)
    
    return True

if __name__ == '__main__':

    List1 = ['s','s','a']
    List2 = ['S','s','a']
    List3 = ['a','b','c']
    List4 = ['a', 'b', 'b', 'c']
    
    print(is_unique(List1))
    print(is_unique(List2))
    print(is_unique(List3))
    print(is_unique(List4))
