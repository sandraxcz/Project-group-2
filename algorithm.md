PROGRAM ChooseBookAtRandom

WRITE "Welcome to Group 2's book recommendation system!"
WRITE "Please choose a number for the genre that you want to read:
WRITE "1. Fantasy, 2. Science fiction. 3. Mystery, 4. Romance, 5. Horror, 6. Adventure, 7. Nonfiction. 8. Historical, 9. Dystopian, 10. Bildungsroman, 11. Memoir"
READ chosenGenreNumber

IF (chosenGenreNumber is 1) THEN
    chosenGenre = "Fantasy"
IF (chosenGenreNumber is 2) THEN
    chosenGenre = "Science Fiction"
IF (chosenGenreNumber is 3) THEN
    chosenGenre = "Mystery"
IF (chosenGenreNumber is 4) THEN
    chosenGenre = "Romance"
IF (chosenGenreNumer is 5) THEN
    chosenGenre = "Horror"
IF (chosenGenreNumber is 6) THEN
    chosenGenre = "Adventure"
IF (chosenGenreNumber is 7) THEN
    chosenGenre = "Nonfiction"
IF (chosenGenreNumber is 8) THEN
    chosenGenre = "Historical"
IF (chosenGenreNumber is 9) THEN
    chosenGenre = "Dystopian"
IF (chosenGenrenumber is 10) THEN
    chosenGenre = "Bildungsroman"
IF (chsoenGenrenumber is 11) THEN
    chosenGenre = "Memoir"
ENDIF

WRITE "Do you want more random recommendations in this genre?"
IF (Yes) THEN
    WRITE "How many recommendations do you want?"
    WRITE "Enter a number of recommendations you want"
    READ num
ELSE IF (No) THEN
    WRITE "Thank you for using our recommendation system!"

ENDIF


    
