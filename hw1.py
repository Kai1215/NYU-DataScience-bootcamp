# 1. function count_vowels(word)
def count_vowels(word):
    sum = 0
    vowels = 'aeiouAEIOU'
    for letter in word:
        if letter in vowels:
            sum += 1
    return sum

word = 'interesting'
print(count_vowels(word))

# 2. Iterate list of animals
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
for number in range(1, 21):
    print(f"{number} is {'odd' if number % 2 else 'even'}")

# 4. sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a, b):
    return a + b

print(sum_of_integers(123,45))