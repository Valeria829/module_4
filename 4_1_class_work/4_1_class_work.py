def palindrome(s):
     print(s[::-1] == s)

while True:
    s = input('введите слово: ')
    palindrome(s)
