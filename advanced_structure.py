from collections import Counter, defaultdict
from dataclasses import dataclass

# Counter
test_string = "abracadabrasadasfrrggevssdf"
char_count = Counter(test_string)
print("Counter test:")
print(f"Character statistics of '{test_string}': {dict(char_count)}")
print(f"The two most common characters: {char_count.most_common(2)}")
print()

# defaultdict
students = [("Ivan", 1), ("alina", 2), ("Max", 1)]
course_groups = defaultdict(list)

for name, course in students:
    course_groups[course].append(name)

print("defaultdict test:")
print("Students are grouped by courses :", dict(course_groups))
print()

#dataclass
@dataclass
class Book:
    title: str
    author: str
    year: int

# Create a list of books
books = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("Don Quixote", "Miguel de Cervantes", 1605),
    Book("War and Peace", "Leo Tolstoy", 1869),
    Book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967)
]

print("dataclass test:")
print("The books before sorting:")
for book in books:
    print(f"  {book.year}: {book.title} - {book.author}")

# Sort by year
books_sorted_by_year = sorted(books, key=lambda x: x.year)

print("\nBooks sorted by year:")
for book in books_sorted_by_year:
    print(f"  {book.year}: {book.title} - {book.author}")