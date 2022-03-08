from Question import Question

question_promts = [
    "What color are apples?\n(A) Red/Green\n (B) Purple \n (C) Orange\n\n",
    "What color are Bnanas?\n(A) Teal\n (B) Magenta \n (C) Yellow\n\n",
    "What color are apples?\n(A) Yellow\n (B) Red \n (C) Blue\n\n"
]


questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Hey you got " + str(score) + "/" + str(len(questions))+ " Questions right")

run_test(questions)