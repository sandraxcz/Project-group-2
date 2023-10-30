PROGRAM ChooseBookAtRandom:

```
WRITE "Welcome to Group 2's book recommendation system!"
WRITE "Please choose a number for the genre that you want to read:"
WRITE "1. Fantasy, 2. Science fiction. 3. Mystery, 4. Romance, 5. Horror, 6. Adventure, 7. Nonfiction. 8. Historical, 9. Dystopian, 10. Bildungsroman, 11. Memoir"
READ chosenGenreNumber

IF (chosenGenreNumber is 1) THEN
    chosenGenre = "Fantasy"
ELSE IF (chosenGenreNumber is 2) THEN
    chosenGenre = "Science Fiction"
ELSE IF (chosenGenreNumber is 3) THEN
    chosenGenre = "Mystery"
ELSE IF (chosenGenreNumber is 4) THEN
    chosenGenre = "Romance"
ELSE IF (chosenGenreNumber is 5) THEN
    chosenGenre = "Horror"
ELSE IF (chosenGenreNumber is 6) THEN
    chosenGenre = "Adventure"
ELSE IF (chosenGenreNumber is 7) THEN
    chosenGenre = "Nonfiction"
ELSE IF (chosenGenreNumber is 8) THEN
    chosenGenre = "Historical"
ELSE IF (chosenGenreNumber is 9) THEN
    chosenGenre = "Dystopian"
ELSE IF (chosenGenrenumber is 10) THEN
    chosenGenre = "Bildungsroman"
ELSE IF (chosenGenrenumber is 11) THEN
    chosenGenre = "Memoir"
ELSE
    WRITE "Please enter a valid number from 1-11."
ENDIF

WHILE user wants book recommendation

    Set bookListPath to 'Project-group-2/data/xml-data.xml'
    Set bookList to importXMLdata(bookListPath)
    Set bookFromChosenGenre to filterBooksByGenre(bookList, chosenGenre)
    Set numberOfBooksGenre to quantityOfbooks(bookFromChosenGenre)

    IF (numberOfBooksGenre > 0) THEN
        set chosenBook to createRandomChoice(bookFromChosenGenre)
        WRITE "Here is a book for you!" chosenBook
    ENDIF

    WRITE "Do you want more random recommendations in this genre? (Yes/No)"
    READ userAnswer

    IF (userAnswer is No) THEN
        EXITWHILE
    ENDIF

    WRITE "How many recommendations do you want (up to 5)?"
    READ num

ENDWHILE

WRITE "Thank you for using our recommendation system!"
```

END.
