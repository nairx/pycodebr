#Accept a word and print the number of vowels
str = input("Enter a word: ")
vowels = "aeiou"
count = 0
for i in str:
    if i.lower() in vowels:
        count = count + 1
print(count)