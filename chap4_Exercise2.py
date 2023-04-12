def is_palindrom(word):
    reversed_str=word[::-1]
    if reversed_str==word:
        return True
    else:
        return False



letter=input("Enter any plandrom letter :")
print(is_palindrom(letter))