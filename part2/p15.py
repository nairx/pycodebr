#Accept a word and print the number of vowels
str = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for i in str:
    if i in vowels:
        count = count + 1
print(count)