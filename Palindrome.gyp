

def is_palindrome(str):
    i = 0
    j = -1

    str = str.lower()

    backward = str[::-1]
    return str == backward

    # while (i < len(str)/2):
    #     if str[i] == str[j]:
    #         i+=1
    #         j-=1
    #     else:
    #         return False
    # return True



print is_palindrome('heeeeeeeeeeh')