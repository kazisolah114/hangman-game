import random
from hangman_art import stages, logo
from hangman_words import hangman_words

print(logo)
lives = 6
random_word = random.choice(hangman_words)
# random_word_list = []
# for letter in random_word:
#     random_word_list.append(letter)
# random.shuffle(random_word_list)
# hint_word = ""
# for letter in random_word_list:
#     hint_word += letter
# print(f"Guess the word: {hint_word}")
word_length = len(random_word)
placeholder = ""
for letter in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter? ")
    result = ""
    for letter in random_word:
        if letter == guess:
            result += letter
            correct_letters.append(letter)
            if guess in correct_letters:
                print(f"You gussed this letter already!")
        elif letter in correct_letters:
            result += letter
        else:
            result += "_"
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost it sucker. Gave over!")
    print(f"You have {lives} more lives left!")
    if "_" not in result:
        game_over = True
        print("Yay you won the game!")
    
    print(result)
    print(stages[lives])