from exams.models import Exam, Question, Answer

# =========================
# Rational Expressions Exam
# =========================

rational_exam = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance — Rational Expressions",
    description="Rational expressions, inequalities, and rational functions practice exam",
    duration_minutes=60,
)

rational_questions = [
    (
        "Which of the following is a rational expression?",
        [
            ("√(1 + x⁴) / (|x| + 1)", False),
            ("(x² + x) / (x² − x)", True),
            ("0.5x / (x² + 1)", False),
            ("2x / (³√(x − 1))", False),
        ],
    ),
    (
        "Given the rational expression (x + 1) / (x² + 7x + 12), what is the domain of the expression?",
        [
            ("{x ∈ ℝ : x ≠ −3 and x ≠ −4}", True),
            ("{x ∈ ℝ : x ≠ −1, x ≠ 3 and x ≠ 4}", False),
            ("{x ∈ ℝ : x ≠ −1, x ≠ −3 and x ≠ −4}", False),
            ("{x ∈ ℝ : x ≠ 3 and x ≠ 4}", False),
        ],
    ),
    (
        "A simplification of the rational expression (1/(x−1) + 1/(x+1)) ÷ (x/(x²−1)) yields:",
        [
            ("(3 − x) / x", False),
            ("3 + x", False),
            ("(3 + x) / x", True),
            ("3 − x", False),
        ],
    ),
    (
        "If P(x) = (6x² + x³ − x⁴) / (x² − 4) and g(x) = (3x³ − 9x²) / (x² + 6x − 16), then which of the following is the solution set of the equation P(x)/g(x) = −3?",
        [
            ("{−1, 1}", False),
            ("{1}", False),
            ("{1, 5}", True),
            ("ℝ \\ {−8, −2, 0, 2, 3}", False),
        ],
    ),
    (
        "The decomposed form of (3x² + 7x + 28) / (x³ + x² + 7x) is:",
        [
            ("4/x + (x − 3)/(x² + x + 7)", True),
            ("4/x − (x − 3)/(x² + x + 7)", False),
            ("3/x + (3 − x)/(x² + x + 7)", False),
            ("4/x − (3 − x)/(x² + x + 7)", False),
        ],
    ),
    (
        "Consider the inequality (x² + 2x − 3)/(x + 2) ≤ 0. Then which of the following is the solution set of the inequality?",
        [
            ("(−∞, −3] ∪ [1, ∞)", False),
            ("[−3, −2) ∪ [1, ∞)", False),
            ("[−3, −2) ∪ (−2, 1]", True),
            ("(−∞, −3] ∪ (−2, 1]", False),
        ],
    ),
    (
        "Which one of the following is true about f(x) = (x³ + 2x² − 2x − 4) / (2x² − 4)?",
        [
            ("The x-intercepts are (−2, 0), (±√2, 0).", True),
            ("y = (1/2)x + 1 is its oblique asymptote.", False),
            ("As x → −∞, f(x) → −∞.", False),
            ("As x → −√2⁻, f(x) → −√2/2 − 1.", False),
        ],
    ),
    (
        "Which of the following is true about the graph of f(x) = (x − 1)/(x² − 1)?",
        [
            ("Its x-intercept is 1.", False),
            ("y = 1 is its horizontal asymptote.", True),
            ("x = 1 is its vertical asymptote.", False),
            ("Its y-intercept is 1.", False),
        ],
    ),
    (
        "If f(x) = (x + 1)/(x − 1) and f(a) = 5, then f(2a) is equal to:",
        [
            ("2", True),
            ("4", False),
            ("6", False),
            ("8", False),
        ],
    ),
    (
        "In one morning, if the shadow of a building is 14 meters long and the shadow of a tree of 15 meters height is 12 meters, then how long is the building in meters?",
        [
            ("28", False),
            ("20", False),
            ("30", False),
            ("17.5", True),
        ],
    ),
]

for question_text, choices in rational_questions:
    q = Question.objects.create(
        exam=rational_exam,
        text=question_text,
    )
    for choice_text, is_correct in choices:
        Answer.objects.create(
            question=q,
            text=choice_text,
            is_correct=is_correct,
        )


# =========================
# Calculus Exam
# =========================

calculus_exam = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance — Calculus",
    description="Derivatives, integrals, and applications of calculus practice exam",
    duration_minutes=60,
)

calculus_questions = [
    (
        "Which one of the following statements is true?",
        [
            ("The indefinite integral of any continuous function is unique.", False),
            ("Integration is the process of finding f(x) from its derivative.", True),
            ("If a is in the domain of f, then f is always differentiable at a.", False),
            ("Integral of the function is an antiderivative of its derivative.", False),
        ],
    ),
    (
        "Which one of the following is the absolute maximum of the function f(x) = (x² − 2x + 4)/(x − 2) on the interval [−3, 1]?",
        [
            ("−19/5", False),
            ("−2", False),
            ("−3", False),
            ("6", True),
        ],
    ),
    (
        "Which of the following is necessarily true?",
        [
            ("∫₋ₐᵃ f(x) dx = 0, if f(x) is an odd function, a ∈ ℝ.", False),
            ("∫₋₃⁴ 7/(x−2) dx = ∫₋₃³ 7/(x−2) dx + ∫₃⁴ 7/(x−2) dx", False),
            ("∫₋₃⁶ 3/(x²−9) dx = ∫₋₃⁰ 3/(x²−9) dx + ∫₀⁶ 3/(x²−9) dx", False),
            ("∫₋ₐᵃ f(x) dx = 2∫₀ᵃ f(x) dx, if f is an even function, a ∈ ℝ.", True),
        ],
    ),
    (
        "If f(x) = (3e⁴ + 5π²) / 2, then what is the value of f'(x)?",
        [
            ("6e³ + 10π", False),
            ("6e³", False),
            ("0", True),
            ("11", False),
        ],
    ),
    (
        "Which of the following is the area (in square units) of the region bounded by the graph of f(x) = x² − 4x + 4, the x-axis between the lines x = 1 and x = 5?",
        [
            ("28/3", False),
            ("40/3", True),
            ("31/3", False),
            ("10", False),
        ],
    ),
    (
        "Which one of the following correctly describes rate of change?",
        [
            ("A positive rate of change is the case when the value of one quantity say x increases and the other related quantity say y decreases.", False),
            ("A negative rate of change is the case when the value of two related quantities x and y decreases at the same time.", False),
            ("A negative rate of change is the case when the value of one quantity say x increases and the other related quantity say y also increases.", False),
            ("A zero rate of change is the case when the value of one quantity x increases and the other related quantity say y remains constant.", True),
        ],
    ),
    (
        "Which of the following best describes the derivative of a function at a point?",
        [
            ("It is the slope of the secant line between two points on the curve.", False),
            ("It is the average rate of change over an interval.", False),
            ("It is the slope of the tangent line to the curve at that point.", True),
            ("It is the area under the curve from 0 to that point.", False),
        ],
    ),
    (
        "If f(x) = √(x + 1/x), then which of the following is equal to f(x)·f'(x)?",
        [
            ("(x² − 1) / (2x²)", True),
            ("(x² − 1) / (2x²)", False),
            ("(x² + 1) / (2x²)", False),
            ("(x² − x) / x", False),
        ],
    ),
    (
        "Which one of the following is true about the function f(x) = 2x³ − 3x² − 36x + 1?",
        [
            ("f is decreasing on (−∞, −2) ∪ (3, ∞)", False),
            ("f(−2) is a local minimum of f.", False),
            ("The critical numbers of f are x = −2, 3.", True),
            ("f(3) is a local maximum.", False),
        ],
    ),
    (
        "Which one of the following is the equation of the tangent line to the graph of f(x) = √x at the point (1, 1)?",
        [
            ("y = (1/2)x + 1/2", True),
            ("y = x − 1", False),
            ("y = (1/2)x + 1", False),
            ("y = (1/2)x − 1/2", False),
        ],
    ),
    (
        "Suppose the side of an isosceles right-angled triangle is increasing at the rate of 4.5 cm/sec. Find the rate at which the area is increasing at the instant when the side is 6 cm.",
        [
            ("54 cm²/sec", False),
            ("13.5 cm²/sec", False),
            ("27 cm²/sec", True),
            ("18 cm²/sec", False),
        ],
    ),
    (
        "Which one of the following is the antiderivative of f(x) = 4x³ − 3x² + 2x − 1?",
        [
            ("F(x) = 12x² − 6x + 2 + c", False),
            ("F(x) = 4x⁴ − 3x³ + 2x² − x + c", False),
            ("F(x) = 4x² − 3x + 2 − x + c", False),
            ("F(x) = x⁴ − x³ + x² − x + c", True),
        ],
    ),
    (
        "Evaluate the definite integral ∫₁⁴ (5/2)x^(3/2) dx",
        [
            ("31", True),
            ("32", False),
            ("15.5", False),
            ("16.5", False),
        ],
    ),
    (
        "Suppose that the speed of a car is given by v(t) = 4t m/s and assume that the distance at t = 0 s is 0 m. What is the total distance covered by the car after t = 6 s?",
        [
            ("24 m", False),
            ("72 m", True),
            ("36 m", False),
            ("60 m", False),
        ],
    ),
    (
        "Which of the following is true about the gradient of a curve?",
        [
            ("It is the number that describes the steepness and direction of the line which intersects the curve at a point.", True),
            ("It is the function that describes the monotonicity of the line which intersects the curve at a point.", False),
            ("It is the function that describes the monotonicity of the line which intersects the curve at two points.", False),
            ("It is the number that describes the steepness and direction of the line which intersects the curve at more than one point.", False),
        ],
    ),
    (
        "Which of the following is the derivative of f(x) = −x / √(x² − 1)?",
        [
            ("f'(x) = 1 / (x² − 1)^(3/2)", True),
            ("f'(x) = (x² − 1) / √(x² − 1)", False),
            ("f'(x) = 1 / √(x² − 1)", False),
            ("f'(x) = x / (x² − 1)^(3/2)", False),
        ],
    ),
    (
        "Which of the following is the interval on which f(x) = 2x⁴ + 4x³ + 2x² + 1 is increasing?",
        [
            ("(−∞, −1) ∪ (1/2, 0)", False),
            ("(−∞, ∞)", False),
            ("(−1, −1/2) ∪ [0, ∞)", True),
            ("(−1/2, 0)", False),
        ],
    ),
    (
        "Which of the following is equal to the indefinite integral ∫ (3x − 1) / (2√x) dx?",
        [
            ("x(√x − 1) + c", False),
            ("√x(x − 1) + c", True),
            ("(1/2)√x(√x − 1)", False),
            ("2√x(x − 1) + c", False),
        ],
    ),
    (
        "What is the average rate of change of f(x) = x³ − 2x over the interval 1 ≤ x ≤ 6?",
        [
            ("37/5", False),
            ("203/5", False),
            ("46", False),
            ("41", True),
        ],
    ),
    (
        "Consider the function f(x) = x³ − 3x² + 3 on (−2, 3). Then which of the following point is local minimum and local maximum of f(x) respectively?",
        [
            ("(3, 3) and (−2, −27)", False),
            ("(2, −1) and (0, 3)", True),
            ("(0, 3) and (2, −1)", False),
            ("(−2, −27) and (0, 3)", False),
        ],
    ),
]

for question_text, choices in calculus_questions:
    q = Question.objects.create(
        exam=calculus_exam,
        text=question_text,
    )
    for choice_text, is_correct in choices:
        Answer.objects.create(
            question=q,
            text=choice_text,
            is_correct=is_correct,
        )