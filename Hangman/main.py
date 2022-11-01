import random
from art import stages

def randomWord():
    wordList = []
    with open('words.txt', 'r') as rf:
        for line in rf:
            wordList.append(line.strip())
        return random.choice(wordList)

def playGame():
    game_is_finished = False
    lives = len(stages) - 1
    chosen_word = randomWord()
    word_length = len(chosen_word)
    letters_guessed = []

    display = []
    for _ in range(word_length):
        display += "_"

    print(f"Guess the {word_length} letter word!")
    print(f"{' '.join(display)}")

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()
        letters_guessed.append(guess)

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"{guess} is not in the word, you have {lives - 1} left")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print(stages[lives])
                print("You lose.")
                callMenu()

        if not "_" in display:
            game_is_finished = True
            print("You win!\n" * 4)
            callMenu()

        print(stages[lives])
        print(f"Letters used \n{' '.join(letters_guessed)}")


def callMenu():
    choice = input("\nEnter 1 to add a word to the wordlist \n"
                   "Enter 2 to print the wordlist \n"
                   "Enter 3 to play the game :")

    if choice == '1':
        with open('words.txt', 'a') as af:
            isWord = False
            addTo = input("Enter a word to add to the wordlist: ").lower()
            for l in addTo:
                if l.isalpha():
                    isWord = True
                else:
                    isWord = False
                    print("Invalid word")
                    break
            if isWord:
                af.write('\n' + addTo)
                print(f"{addTo} had been added to the wordlist")
        callMenu()

    elif choice == '2':
        with open('words.txt', 'r') as rf:
            for line in rf:
                print(line, end='')
        callMenu()
    elif choice == '3':
        playGame()

    else:
        print("\nInvalid option select again")
        callMenu()


callMenu()
