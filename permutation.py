def check_permutation(st1, st2):
    # First, check if the lengths of the strings are equal
    if len(st1) != len(st2):
        return False
    
    # Sort both strings and compare them
    return sorted(st1) == sorted(st2)

if __name__ == "__main__":
    st1 = 'ABC'
    st2 = 'BAC'
    st3 = 'CBA'
    st4 = 'ABCD'

    print(check_permutation(st1, st2))  
    print(check_permutation(st1, st3))  
    print(check_permutation(st1, st4))  


