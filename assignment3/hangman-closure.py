def make_hangman(secret):
    guesses = []
    def hangman(letter):
        guesses.append(letter.lower())
        display = ''.join([c if c in guesses else '_' for c in secret.lower()])
        print(display)
        return all(c in guesses for c in secret.lower())
    return hangman
word = input("Enter secret word: ")
game = make_hangman(word)
while not game(input("Guess a letter: ")):
    pass
print("You won!")
