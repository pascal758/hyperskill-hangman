import random

print('H A N G M A N')
while True:
    choose = input('Type "play" to play the game, "exit" to quit:')
    if choose == 'play':
        list_words = ['python', 'java', 'kotlin', 'javascript']

        random_word = random.choice(list_words)

        word_list = list('-' * len(random_word))

        attempt = 8
        answer_set = set()

        while attempt > 0:
            print()
            print(''.join(word_list))
            answer = input('Input a letter: ')
            if answer in answer_set:
                print("You've already guessed this letter")
            elif len(answer) != 1:
                print('You should input a single letter')
            elif not str.islower(answer):
                print('Please enter a lowercase English letter')
            elif answer in random_word and answer not in answer_set:
                for x in range(len(random_word)):
                    if answer == random_word[x]:
                        word_list[x] = answer
                answer_set.add(answer)
            elif answer not in answer_set:
                print("That letter doesn't appear in the word")
                attempt -= 1
                answer_set.add(answer)

            if '-' not in word_list:
                print('You guessed the word!')
                print('You survived!')
                break
        else:
            print('You lost!')
    elif choose == 'exit':
        break
