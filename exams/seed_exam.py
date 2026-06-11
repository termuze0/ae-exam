from exams.models import Exam, Question, Answer


def seed(exam, questions):
    for question_text, choices in questions:
        q = Question.objects.create(exam=exam, text=question_text)
        for choice_text, is_correct in choices:
            Answer.objects.create(question=q, text=choice_text, is_correct=is_correct)



math_questions_units3_4 = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Mathematics Units 3 & 4",
    description="ASTU Excellence Team entrance exam — matrices, determinants,",
    duration_minutes=60,
    is_active=True,
)
 
# Each entry: (question_text, [(answer_text, is_correct), ...]
question1 =[
 
    # Q1 — Matrix equality
    (
        "What is the value of b for which the matrices "
        "A = [[1, 2], [3, -1]] and B = [[a-b, 2], [a, -1]] are equal?",
        [
            ("1", False),
            ("2", True),
            ("3", False),
            ("5", False),
        ],
    ),
 
    # Q2 — Matrix transpose & operations
    (
        "Let A = [[1, 2], [3, -1]] and B = [[0, 2], [1, 0]]. "
        "Which of the following statements is true?",
        [
            ("(Aᵀ + B)ᵀ = [[1, 3], [5, -1]]", True),
            ("Aᵀ - B = [[1, 1], [1, 1]]", False),
            ("(2AB)ᵀ = [[4, 4], [-2, 12]]", False),
            ("(1/2)(A - Aᵀ) = (1/2)[[0, 1], [-1, 0]]", False),
        ],
    ),
 
    # Q3 — Matrix theorems
    (
        "Which of the following is true?",
        [
            ("If A and B are square matrices, then A² - B² = (A - B)(A + B).", False),
            ("If A and B are invertible matrices, then (AB)⁻¹ = B⁻¹A⁻¹.", True),
            ("If A is a 3×4 matrix and B is a 4×3 matrix, then AB is a 4×4 matrix.", False),
            ("If A and B are square matrices, then (AB)² = A²B².", False),
        ],
    ),
 
    # Q4 — Minor and cofactor
    (
        "Let A = [[2, 0, 5], [1, -5, 3], [1, 4, 6]]. "
        "What are the values of M₂₃ and C₂₃ respectively?",
        [
            ("8, -8", True),
            ("-8, 8", False),
            ("6, -6", False),
            ("-6, 6", False),
        ],
    ),
 
    # Q5 — System of linear equations
    (
        "Which one of the following is the solution set of the system?\n"
        "  x + y + z = 1\n"
        "  2x - y + z = 0\n"
        "  x + 2y - z = -3",
        [
            ("{(-1, 0, 2)}", True),
            ("Empty set (no solution)", False),
            ("{(-t, 0, 2t) : t is any real number}", False),
            ("{(-1, 0, 1)}", False),
        ],
    ),
 
    # Q6 — Cramer's Rule
    (
        "Consider the system:\n"
        "  x + y - z = 1\n"
        "  2x + z = 4\n"
        "  y - z = 5\n"
        "What is the value of x using Cramer's Rule?",
        [
            (
                "x = det([[1,1,-1],[4,0,1],[5,1,-1]]) / det([[1,1,-1],[2,0,1],[0,1,-1]])  "
                "(constants in column 1 — wrong matrix)",
                False,
            ),
            (
                "x = det([[1,1,1],[2,0,4],[0,1,5]]) / det([[1,1,-1],[2,0,1],[0,1,-1]])  "
                "(constants in column 3)",
                False,
            ),
            (
                "x = det([[1,1,-1],[2,4,1],[0,5,-1]]) / det([[1,1,-1],[2,0,1],[0,1,-1]])  "
                "(constants in column 2)",
                False,
            ),
            (
                "x = det([[1,1,-1],[4,0,1],[5,1,-1]]) / det([[1,1,-1],[2,0,1],[0,1,-1]])  "
                "(constants replace column 1 correctly)",
                True,
            ),
        ],
    ),
 
    # Q7 — Matrix inverse
    (
        "Find the inverse of A = [[2, 4, 2], [3, 1, 1], [1, 0, 1]].",
        [
            ("A⁻¹ = [[1/8, -1/2, 1/4], [-1/4, 0, 1/2], [-1/8, 1/2, -5/4]]", False),
            ("A⁻¹ = [[-2, -4, -2], [-3, -1, -1], [-1, 0, -1]]", False),
            ("A⁻¹ = [[-1/8, 1/2, -1/4], [1/4, 0, -1/2], [1/8, -1/2, 5/4]]", True),
            ("A⁻¹ = [[1/8, 1/2, 1/4], [1/4, 0, 1/2], [1/8, 1/2, 5/4]]", False),
        ],
    ),
 
    # Q8 — Determinant properties
    (
        "If A and B are square matrices of order 3 with det(A) = 4 and det(B) = 5, "
        "which of the following is true?",
        [
            ("det(3ABᵀ) = 540", True),
            ("det(2AB) = 40", False),
            ("det(4A) = 16", False),
            ("det(2B²) = 50", False),
        ],
    ),
 
    # Q9 — Inverse determinant
    (
        "If a matrix A is invertible, what is the determinant of A⁻¹?",
        [
            ("det(A)", False),
            ("-det(A)", False),
            ("1 / det(A)", True),
            ("(det(A))²", False),
        ],
    ),
 
    # Q10 — Singular matrix
    (
        "The value of t for which the matrix "
        "[[t, t, -1], [t, 2, -3], [2, 3, -4]] is singular is",
        [
            ("1", True),
            ("2", False),
            ("-1", False),
            ("3", False),
        ],
    ),
 
    # Q11 — Symmetric matrix
    (
        "Let P be a square matrix of order n and Pᵀ its transpose. "
        "If P is a symmetric matrix, which of the following is true?",
        [
            ("P = -(1/2)Pᵀ", False),
            ("P = (1/2)Pᵀ", False),
            ("P = -Pᵀ", False),
            ("P = Pᵀ", True),
        ],
    ),
 
    # Q12 — Exponent simplification
    (
        "Which of the following is the simplification of "
        "( 3^(2/5) / (2^(4/3) × 4^(1/5)) )^(-10/9) × 81?",
        [
            ("49/22", False),
            ("1/2", True),
            ("17/22", False),
            ("3/4", False),
        ],
    ),
 
    # Q13 — Exponential equation
    (
        "The solution set of the equation "
        "s^(1/4) × (1/16)^(1/2 - x) = 2 × (0.125)^x is",
        [
            ("{0}", False),
            ("{-1/2}", False),
            ("{2}", False),
            ("{3/5}", True),
        ],
    ),
 
    # Q14 — Logarithmic equation
    (
        "The solution set of log(x² - 3) = 2·log(x - 1) is",
        [
            ("{2}", True),
            ("{1/2}", False),
            ("{4}", False),
            ("Empty set (no solution)", False),
        ],
    ),
 
    # Q15 — Logarithm change of base
    (
        "If log base √3 of (3a/9) = x, then the value of log base 3 of a is equal to",
        [
            ("1/x", False),
            ("x / (6 - x)", False),
            ("(6 - x) / x", False),
            ("6/x", True),
        ],
    ),
 
    # Q16 — Logarithm computation
    (
        "If log(50) = 1.699, then log(0.00025) =",
        [
            ("-4.398", False),
            ("-3.602", True),
            ("0.602 + (-3)", False),
            ("0.398 + (-5)", False),
        ],
    ),
 
    # Q17 — Compound interest
    (
        "If Birr 20,000 is deposited in a bank at a rate of 12% interest compounded "
        "monthly, how long will it take to double the amount?",
        [
            ("5.81 years", True),
            ("5 years", False),
            ("7.59 years", False),
            ("6 years", False),
        ],
    ),
 
    # Q18 — Trigonometric identities
    (
        "Which of the following is true about the trigonometric values of the given pairs of angles?",
        [
            ("sin(75°) = cos(105°)", False),
            ("tan(75°) = tan(105°)", False),
            ("sin(120°) = sin(60°)", True),
            ("cos(120°) = cos(60°)", False),
        ],
    ),
 
    # Q19 — Slope and angle
    (
        "The slope of the line that makes an angle of 135° with the positive x-axis is equal to",
        [
            ("3", False),
            ("1", False),
            ("-1", True),
            ("2", False),
        ],
    ),
 
    # Q20 — Trigonometric ratios
    (
        "If sin(θ) = 3/5 and θ is a first quadrant angle, what is the value of sec(θ)?",
        [
            ("5/4", True),
            ("5/3", False),
            ("-5/4", False),
            ("-5/3", False),
        ],
    ),
 
    # Q21 — Properties of tan x
    (
        "Which one of the following is true about the function f(x) = tan(x)?",
        [
            ("f is a periodic function with period π/2.", False),
            ("The domain of f is all real numbers except -π/2 and π/2.", False),
            ("The graph of f intersects the y-axis at (π/2, 0).", False),
            ("The range of f is the set of all real numbers.", True),
        ],
    ),
 
    # Q22 — Cotangent of large angle
    (
        "Which one of the following is equal to cot(1755°)?",
        [
            ("√3", False),
            ("1", False),
            ("-√3", False),
            ("-1", True),
        ],
    ),
 
    # Q23 — Cosine from tangent (fourth quadrant)
    (
        "x is an angle in the fourth quadrant. When tan(x) = -2, what is the value of cos(x)?",
        [
            ("√5", False),
            ("1/√5", True),
            ("-√5", False),
            ("1/25", False),
        ],
    ),
 
    # Q24 — Angle of elevation / tree height
    (
        "Find the height of a tree which casts a shadow of 12.4 m when the "
        "angle of elevation of the sun is 52°.",
        [
            ("16.9 m", False),
            ("20 m", False),
            ("15.9 m", True),
            ("25.6 m", False),
        ],
    ),
]
 

seed(math_questions_units3_4, question1)