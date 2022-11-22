import random


def read_words_from_file(path_to_file='words.txt'):
    """
    Function is reading a text file and returning the list of lines
    """
    with open(path_to_file, 'rt') as words_file:
        return words_file.readlines()


def get_record_for_player(current_player, path_to_file='history.txt'):
    """
    The function is returning best score for current player
    """
    with open(path_to_file, 'rt') as history_file:
        record_of_player = 0
        count_of_rounds = 0
        for line in history_file:
            current_score_list = line.split(',')

            if current_score_list[0] == current_player:
                current_score = int(current_score_list[1].replace('\n', ''))
                count_of_rounds += 1

            if current_score > record_of_player:
                record_of_player = current_score

    return count_of_rounds, record_of_player


def save_round_result_to_file(current_player, current_game_score, path_to_file='history.txt'):
    """
    The function is appending score of current round for current player in text file
    """
    with open(path_to_file, 'a') as history_file:
        history_file.write(f'{current_player},{current_game_score}\n')


player_name = input('What is your name:\n')

words = read_words_from_file()
answers = []
points = 0

for word in words:
    base_word = word.replace('\n', '')  # clear the word from \n
    shuffled_word = ''.join(random.sample(base_word, len(base_word)))
    current_answer = input(f'Guess the word: {shuffled_word}\n')
    if current_answer == base_word:
        print('Right, you get 10 points')
        points += 10
    else:
        print(f'\nIt is wrong! Right answer is {word}\n')

print(f'Round ended, your score is {points} points')

save_round_result_to_file(player_name, points)

current_player_record = get_record_for_player(player_name)

print(f'Total rounds is : {current_player_record[0]}\nAnd your personal record is: {current_player_record[1]}\n')
