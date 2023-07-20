def palindrome(s):
     return(s[::-1] == s)

while True:
    s = input('введите слово: ')
    palindrome(s)
