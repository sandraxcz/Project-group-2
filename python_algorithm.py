def importXMLdata(path):
    pass

def filterBooksByGenre(bookList, chosenGenre):
    pass

def quantityOfBooks(bookList):
    pass

def createRandomChoice(bookList):
    pass

print("Welcome to Group 2's book recommendation system!")
print("Please choose a number for the genre that you want to read:")
print("1. Fantasy, 2. Science fiction, 3. Mystery, 4. Romance, 5. Horror, 6. Adventure, 7. Nonfiction, 8. Historical, 9. Dystopian, 10. Bildungsroman, 11. Memoir")

chosenGenreNumber = int(input("Enter the number for your chosen genre: "))

genres = {
    1: "Fantasy",
    2: "Science Fiction",
    3: "Mystery",
    4: "Romance",
    5: "Horror",
    6: "Adventure",
    7: "Nonfiction",
    8: "Historical",
    9: "Dystopian",
    10: "Bildungsroman",
    11: "Memoir"
}

if chosenGenreNumber in genres:
    chosenGenre = genres[chosenGenreNumber]
else:
    print("Please enter a valid number from 1-11.")
    exit()

while True:
    bookListPath = 'Project-group-2/data/xml-data.xml'
    bookList = importXMLdata(bookListPath)
    bookFromChosenGenre = filterBooksByGenre(bookList, chosenGenre)
    numberOfBooksGenre = quantityOfBooks(bookFromChosenGenre)

    if numberOfBooksGenre == int < 0:
        chosenBook = createRandomChoice(bookFromChosenGenre)
        print("Here is a book for you:", chosenBook)

    userAnswer = input("Do you want more random recommendations in this genre? (Yes/No) ")
    if userAnswer.lower() != "yes":
        break

    num = input("How many recommendations do you want (up to 5)? ")


print("Thank you for using our recommendation system!") 
