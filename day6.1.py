# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import re


def calculate_answered_questions(question):
    regex = re.compile('[^a-z]')
    consolidated_question = regex.sub('', question)
    question_without_duplicates = set(consolidated_question)
    print(question_without_duplicates)
    return len(question_without_duplicates)


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
