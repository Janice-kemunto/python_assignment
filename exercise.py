
# Creating a tuple of favorite books
favorite_books = ("Steps to Christ", "Desire of Ages", "Patriachs and Prophets", "Ministry of Healing", "Daughters of  God ")

# Printing each book name on a separate line using a for loop
for book in favorite_books:
    print(book)

# Using a dictionary to store information about a person
person = {}
person['name'] = input("Jane Mukami: ")
person['age'] = input("20: ")
person['favorite_color'] = input("Black:")

# Printing the dictionary
print(person)

# Accepting user input to create two sets of integers
set1 = set(map(int, input("500: ").split()))
set2 = set(map(int, input("10,000: ").split()))

# Creating a new set containing only common elements
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)
