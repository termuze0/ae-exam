from exams.models import Exam, Question, Answer

exam = Exam.objects.create(
    title="Basic Mathematics Exam",
    description="Practice mathematics questions",
    duration_minutes=30
)

questions = [
    {
        "question": "What is 2 + 2?",
        "choices": [
            ("3", False),
            ("4", True),
            ("5", False),
            ("6", False),
        ],
    },
    {
        "question": "What is 5 × 3?",
        "choices": [
            ("10", False),
            ("12", False),
            ("15", True),
            ("20", False),
        ],
    },
    {
        "question": "What is 20 ÷ 4?",
        "choices": [
            ("4", False),
            ("5", True),
            ("6", False),
            ("8", False),
        ],
    },
    {
        "question": "What is 9 + 8?",
        "choices": [
            ("15", False),
            ("16", False),
            ("17", True),
            ("18", False),
        ],
    },
    {
        "question": "What is 12 - 5?",
        "choices": [
            ("6", False),
            ("7", True),
            ("8", False),
            ("9", False),
        ],
    },
    {
        "question": "What is 7 × 6?",
        "choices": [
            ("36", False),
            ("40", False),
            ("42", True),
            ("48", False),
        ],
    },
    {
        "question": "What is the square root of 81?",
        "choices": [
            ("7", False),
            ("8", False),
            ("9", True),
            ("10", False),
        ],
    },
    {
        "question": "What is 15 + 10?",
        "choices": [
            ("20", False),
            ("25", True),
            ("30", False),
            ("35", False),
        ],
    },
    {
        "question": "What is 100 ÷ 10?",
        "choices": [
            ("5", False),
            ("8", False),
            ("10", True),
            ("12", False),
        ],
    },
    {
        "question": "What is 11 × 11?",
        "choices": [
            ("111", False),
            ("121", True),
            ("131", False),
            ("141", False),
        ],
    },
]

for item in questions:
    question = Question.objects.create(
        exam=exam,
        text=item["question"]
    )

    for answer_text, is_correct in item["choices"]:
        Answer.objects.create(
            question=question,
            text=answer_text,
            is_correct=is_correct
        )

print("10 questions created successfully.")