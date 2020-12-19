# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import re

from collections import Counter


def calculate_answered_questions(question):
    questions = question.split("\n")
    question_last_index = len(questions) - 1
    if questions[question_last_index] == "\n" or questions[question_last_index] == "":
        questions.pop(len(questions) - 1)
    counter = Counter(questions[0])

    for words in questions:
        print(words)
        counter &= Counter(words)

    print(counter)
    print(len(counter))
    print("----")
    return len(counter)

def calculate_test():
    assert calculate_answered_questions("abcdefgabc") == 7


def calculate_total_answered_questions():
    complete_answered_questions = ""
    count = 0
    file = open("./inputs/day6.bat", "r")

    for line in file:
        if line == "\n":
            count += calculate_answered_questions(complete_answered_questions)
            complete_answered_questions = ""
        else:
            complete_answered_questions += str(line)

    count += calculate_answered_questions(complete_answered_questions)
    print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_total_answered_questions()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
