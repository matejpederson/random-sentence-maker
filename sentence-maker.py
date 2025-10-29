import os
import random

# opens file, gets noun/adjective/verb data, then returns each as a list
def get_data_from_file(filename):
    noun_list = [] # list to be returned
    noun_line = '' # line of file with nouns
    adjective_list = []
    adjective_line = ''
    verb_list = []
    verb_line = ''
    file_handler = open(filename, 'r')
    data = file_handler.readlines() # each line of file is stored as list item
    file_handler.close()
    for i in range(0, len(data)): # iterates though list of lines and stores wanted lines as strings
        line = data[i].strip()
        if line == 'Nouns:':
            noun_line = data[i+1].strip()
        elif line == 'Adjectives:':
            adjective_line = data[i+1].strip()
        elif line == 'Verbs:':
            verb_line = data[i+1].strip()

    noun_list = noun_line.split(',') # splits string into list items by comma
    for i in range(0, len(noun_list)): noun_list[i] = noun_list[i].strip().lower()
    # strips any leading or trailing white spaces and makes lowercase

    adjective_list = adjective_line.split(',')
    for i in range(0, len(adjective_list)): adjective_list[i] = adjective_list[i].strip().lower()

    verb_list = verb_line.split(',')
    for i in range(0, len(verb_list)): verb_list[i] = verb_list[i].strip().lower()

    return noun_list, adjective_list, verb_list

# takes list of nouns, adjectives, and verbs then returns a random word from each
def get_random_words(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def sentence1(noun_list, adjective_list, verb_list):
    noun = get_random_words(noun_list)
    adjective = get_random_words(adjective_list)
    verb = get_random_words(verb_list)
    print(f'The {adjective} {noun} will {verb}')



def main():
    file = 'word-input.txt'
    if not os.path.exists(file):
        print(f'{file} not found')
        exit()

    noun_list, adjective_list, verb_list = get_data_from_file(file)
    print(noun_list)
    print(adjective_list)
    print(verb_list)
    print()

    sentence1(noun_list, adjective_list, verb_list)

main()
