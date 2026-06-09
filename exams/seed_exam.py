from exams.models import Exam, Question, Answer


def seed(exam, questions):
    for question_text, choices in questions:
        q = Question.objects.create(exam=exam, text=question_text)
        for choice_text, is_correct in choices:
            Answer.objects.create(question=q, text=choice_text, is_correct=is_correct)


# =========================
# Aptitude Entrance Exam
# =========================

aptitude_entrance = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Aptitude",
    description="Aptitude entrance exam — verbal and quantitative reasoning",
    duration_minutes=120,
)

aptitude_entrance_questions = [
    ("If two days after tomorrow is four days before Saturday, what day is it today?", [("Friday", False), ("Saturday", False), ("Sunday", False), ("Monday", True)]),
    ("Gad is older than Dan and Dan is older than Betti. With Senni being older than Dan and younger than Gad, who is the youngest?", [("Betti", True), ("Senni", False), ("Gad", False), ("Dan", False)]),
    ("Aki is Bali's sister. Yaya is Bali's mother. Lema is Yaya's father. Gette is Lema's mother. Then how is Aki related to Lema?", [("daughter", False), ("granddaughter", True), ("grandson", False), ("grandmother", False)]),
    ("Statement I: All football players are sportspersons. Statement II: All sportspersons are fit. The conclusion 'Some football players are fit' is:", [("Conclusion: Some football players are fit.", False), ("incorrect", False), ("reasonably correct", True), ("appropriate", False)]),
    ("How many months have a twenty-eighth day?", [("seven months", False), ("twelve months", True), ("one month", False), ("two months", False)]),
    ("Which of the following can be rearranged into a 5-letter English word?", [("PYRIO", False), ("DWAEP", True), ("GOFAT", False), ("PASEH", False)]),
    ("Passage I: What is the matter with our reading is casualness, languor, preoccupation. We don't give the book a chance. We don't put ourselves at the disposal of the book. It is impossible to read properly without using all one's engine power. If we are not tired after reading, common sense is not in us. How one should grapple with a superior and not be out of breath? But even if we read with the whole force of our brain, and do nothing else, common sense is still not in us, while sublime conceit is. For we are assuming that, without further trouble, we can possess, co-ordinate, and assimilate all the ideas and sensations rapidly offered to us by a mind greater than our own. The assumption has only to be stated in order to appear in its monstrous absurdity. Hence, it follows that something remains to be done; This something is the act of reflection. Reading without subsequent reflection is ridiculous; it is equally a proof of folly and vanity.\n\nWhat is described as an absurd assumption about reading according to the passage?", [("Reading does not require physical effort.", False), ("All books are equally valuable.", False), ("Ideas can be instantly absorbed and organized.", True), ("Superior minds are easy to understand.", False)]),
    ("Which of the ideas is used as evidence for the absurd assumption about reading?", [("Line 3-4 [If we are not ... is not in us.]", False), ("Line 7-9 [For we ... greater than our own.]", True), ("Line 4 [tired after reading ... disposal of the book.]", False), ("Line 1 [What is the ... preoccupation.]", False)]),
    ("Why does the author emphasize the act of reflection?", [("To complete the reading process.", True), ("To simplify the ideas encountered.", False), ("To improve intellectual superiority.", False), ("To make reading more enjoyable.", False)]),
    ("Which of the ideas is used as evidence for the importance of reflection?", [("Line 10 [The assumption ... absurdity.]", False), ("Line 12 [Reading without ... ridiculous.]", True), ("Line 4 [tired after reading ... not in us.]", False), ("Line 1 [What is the ... preoccupation.]", False)]),
    ("Identify the grammatically correct sentence:", [("One of all-time greatest payer have recently retired from football.", False), ("One of all-time greatest payers have recently retired from football.", False), ("One of all-time greatest payer has recently retired from football.", True), ("One of all-time greatest payers has recently retired from football.", False)]),
    ("Identify the grammatically correct sentence:", [("If you'll not feel well, you'd better go to clinic.", False), ("If you're not feeling well, you'd better go to clinic.", True), ("If you'll not feel well, you better go to clinic.", False), ("If you're not feeling well, you would better go to clinic.", False)]),
    ("Identify the grammatically correct sentence:", [("There school takes only twenty minutes on foot.", False), ("Theirs school takes only twenty minutes on foot.", False), ("Their school takes only twenty minutes on foot.", True), ("They're school takes only twenty minutes on foot.", False)]),
    ("Identify the grammatically correct sentence:", [("I wanted to first take shower and then eat snack.", True), ("I wanted first take shower and then eat snack.", False), ("I wanted to first take shower and then ate snack.", False), ("I wanted to first take shower and then eating snack.", False)]),
    ("Choose the word that does NOT fit the group: Monogamy, Polygamy, Polyglot, Polyandry", [("Monogamy", False), ("Polygamy", False), ("Polyglot", True), ("Polyandry", False)]),
    ("Choose the word that does NOT fit the group: Election, Ballot-box, Signal-box, Voting", [("Election", False), ("Ballot-box", False), ("Signal-box", True), ("Voting", False)]),
    ("Choose the word that does NOT fit the group: Tiptoeing, Flying, Strolling, Striding", [("Tiptoeing", False), ("Flying", True), ("Strolling", False), ("Striding", False)]),
    ("Choose the word that does NOT fit the group: Yacht, Ship, Vehicle, Boat", [("Yacht", False), ("Ship", False), ("Vehicle", True), ("Boat", False)]),
    ("AUTOMOBILE : GARAGE :: Hangar : ________", [("Deck", False), ("Truck", False), ("Train", False), ("Airplane", True)]),
    ("KEY : LOCK :: Computer : ________", [("Server", False), ("Screen", False), ("Monitor", False), ("Password", True)]),
    ("NEST : BIRD :: Lion : ________", [("Backyard", False), ("Den", True), ("Hive", False), ("Cave", False)]),
    ("PHYSICIAN : HOSPITAL :: School : ________", [("Administrator", False), ("Student", False), ("Supervisor", False), ("Teacher", True)]),
    ("Choose the closest synonym for: PHONEY", [("Fake", True), ("Funny", False), ("Genuine", False), ("Authentic", False)]),
    ("Choose the closest synonym for: HUMOROUS", [("Satiating", False), ("Satisfying", False), ("Amusing", True), ("Doubting", False)]),
    ("Choose the closest synonym for: THEFT", [("Burglary", True), ("Hypocrisy", False), ("Gossip", False), ("Suspicion", False)]),
    ("Choose the word most nearly opposite in meaning to: FONDLY", [("Affectionate", False), ("Sociable", False), ("Hatred", True), ("Agreeable", False)]),
    ("Choose the word most nearly opposite in meaning to: INVINCIBLE", [("Breakable", False), ("Debatable", False), ("Visible", False), ("Conquerable", True)]),
    ("Choose the word most nearly opposite in meaning to: SUBORDINATE", [("Superior", True), ("Retainer", False), ("Soldier", False), ("Inferior", False)]),
    ("Passage II: If you want transition from being an employee to an employer, the first step is to serve your current employer as you would wish to be served. Most successful employers today have risen through the ranks, relying on their ability to manage and direct others effectively by suppressing the vices of employers. They started with no more opportunities than you have now. There are people in your community who could benefit from your skills and vice versa. For example, Mr. John Smith wants to sell his grocery store and start a movie theater, while someone else with a movie theater might want to trade for a grocery store. If you can connect these two individuals, you will serve both and earn a commission in the process.\n\nIn Paragraph 2, the phrase 'these two individuals' refers to:", [("John Smith & the person in movie industry.", True), ("the grocery store and the movie theatre.", False), ("the employer and the employee.", False), ("people and the community as a whole.", False)]),
    ("What does 'most successful employers today have risen through the ranks, relying on their ability to manage and direct others effectively' imply?", [("Every successful employer is the result of his/her hard work and diligence.", False), ("Having different ranks and rewards is the real manifestation of successful employers.", False), ("All successful employers today have reached their level passing through lots of ups and downs.", False), ("Most successful employers have proven their leadership ability through their journey.", True)]),
    ("The main intent of the writer in the text is to imply that:", [("the transition from employee to employer does not require much effort except having the interest.", False), ("smooth transition from being an employer to employee is more of a matter of destiny than hard work.", False), ("most successful employers are those who have achieved their dreams through trade-off.", False), ("there are steps that one needs to undergo in the transition from employee to employer.", True)]),
    ("According to the passage, what does the word 'vices' most likely denote?", [("deputies", False), ("strengths", False), ("weaknesses", True), ("ambitions", False)]),
    ("Choose the word which can replace the bold term: The man was killed in a car accident. His body was dragged from the burning wreckage of his car.", [("remains", True), ("fire", False), ("backseats", False), ("wheels", False)]),
    ("Choose the word which can replace the bold term: Harvard is one of the most prestigious universities in the USA.", [("privileged", False), ("admired", True), ("furnished", False), ("expensive", False)]),
    ("Choose the word which can replace the bold term: The government has just repealed the law segregating public facilities so that there will be no longer discrimination.", [("approved", False), ("renewed", False), ("signed", False), ("cancelled", True)]),
    ("How many triangles are there in the diagram?", [("18", True), ("14", False), ("16", False), ("12", False)]),
    ("Which one of the following statements is true?", [("Every integer number can be numerator of a rational number.", True), ("Every non-negative integer is a natural number.", False), ("The intersection of the set of integers and the set of irrational numbers is non-empty set.", False), ("The sum of two irrational numbers is irrational number.", False)]),
    ("If f(x) = sin(πx) + e^(x²) + |x| + x³ and g(x) = cos(πx) + ln(x + 1) + x, then what is the value of f(1) − 2g(0)?", [("e", True), ("ln 2", False), ("0", False), ("e + 2", False)]),
    ("A student makes a glass of juice and used half of the glass with avocado, one third of the remaining half with mangoes and the rest is filled by banana and papaya with the same proportion. Which one of the following is the ratio of bananas to avocadoes in the glass?", [("1:6", False), ("1:2", False), ("1:3", True), ("2:3", False)]),
    ("Which one of the following is the largest number?", [("6th root of 5", True), ("36th root of 2", False), ("12th root of 11", False), ("64th root of 3", False)]),
    ("Two pipes A and B are used to fill a water tank. Pipe A can fill the tank in 3 hours, and pipe B can fill the same tank in 6 hours. How long will it take in hours to fill the tank if both pipes are opened at the same time?", [("5", False), ("4", False), ("9", False), ("2", True)]),
    ("A milk factory has only two pipe machines used to fill bottles for market. The old and new machines can fill 35 and 50 bottles per hour, respectively, and a total of 590 bottles are filled every day. One day the old machine was broken after working for 4 hours. How long will it take in hours for the new machine to fill the remaining bottles on that day?", [("8", False), ("9", True), ("13", False), ("7", False)]),
    ("If a spherical soccer ball has a volume of 36π cm³, then which one of the following is the surface area of the ball?", [("(16π)/3", False), ("12π", False), ("36π", True), ("(32π)/3", False)]),
    ("A ball is shot into the air from the top of the building. The height in meters is given by h(t) = kt − t² + 30, where t is the time taken in seconds. What is the possible value of k if the maximum value of height from the ground is 34?", [("√2", False), ("4", True), ("5", False), ("2", False)]),
    ("A farmer has ten cows. Every day, he receives the same amount of milk in liters from each cow. One day, due to the food supply, he received half of the daily amount of milk from four cows; he received three-fourth of the daily amount of milk from three cows, and no milk from the other three cows. In total, he didn't receive ninety-two liters of milk on that day. How many liters of milk did he receive on that particular day?", [("92", False), ("16", False), ("160", False), ("68", True)]),
    ("Study Patterns recorded for 32 days: 2 hrs (10 days), 4 hrs (7 days), 6 hrs (7 days), 8 hrs (5 days), 10 hrs (3 days). How many days did the student study more than the average amount of study?", [("18", False), ("8", False), ("17", False), ("15", True)]),
    ("Study Patterns recorded for 32 days: 2 hrs (10 days), 4 hrs (7 days), 6 hrs (7 days), 8 hrs (5 days), 10 hrs (3 days). How many days did the student study less than 8 hours?", [("5", False), ("2", False), ("24", True), ("12", False)]),
    ("Study Patterns recorded for 32 days: 2 hrs (10 days), 4 hrs (7 days), 6 hrs (7 days), 8 hrs (5 days), 10 hrs (3 days). Which time in hours is the median amount of study?", [("6", False), ("8", False), ("24", False), ("4", True)]),
    ("If −x + 2y = 4, then what is the value of (25^y) / (5^x)?", [("125", False), ("625", True), ("5", False), ("25", False)]),
    ("A woman burns 416 calories in an hour exercise at a fitness center. If she burns 10 calories per minute swimming in the water and 6 calories per minute pedaling on the stationary bike, then how many minutes of the hour does she spend exercising in the water?", [("56", False), ("14", True), ("60", False), ("46", False)]),
    ("Which one of the following is the domain of g(x) = ln(1 − x) + ln(x)?", [("(0, ∞)", False), ("R \\ {(−1, 0)}", False), ("(0, 1)", True), ("(1, ∞)", False)]),
    ("How many days are there from the first day of March to the last day of May?", [("89", False), ("92", True), ("91", False), ("90", False)]),
    ("A corporation pays ten employees a total of Birr 100,000 every month. Six out of ten employees receives less than Birr 10,000 per month. Compare: Quantity P (average monthly payment) vs Quantity Q (median monthly payment).", [("Quantity P is greater than Quantity Q.", True), ("Quantity P is less than Quantity Q.", False), ("The two quantities cannot be compared.", False), ("The two quantities are equal.", False)]),
    ("Consider the lengths of the sides of a triangle x, y, z. Compare Quantity P: 3x + y − z vs Quantity Q: 4x.", [("Quantity P is less than Quantity Q.", True), ("Quantity P is greater than Quantity Q.", False), ("The two quantities cannot be compared.", False), ("The two quantities are equal.", False)]),
    ("Which one of the following is true about the function f(x) = x^(2/5)?", [("The domain of f is {x ∈ R | x ≥ 0}", False), ("The range of f is {y ∈ R | y ≥ 0}", True), ("The range of f is {y | y ∈ R}", False), ("The domain of f is {x ∈ R | x ≤ 0}", False)]),
    ("What is the value of z in the sequence 1, 2, 4, 8, 10, 20, 22, z, ...?", [("44", True), ("24", False), ("32", False), ("40", False)]),
    ("An engineer places black ceramics along both diagonals of a 6×6 square floor (area 36 m², each tile 1 m²) and white ceramics on the rest. What is the ratio of black to white ceramics used?", [("1:6", False), ("1:2", False), ("1:5", True), ("4:5", False)]),
    ("A daily profit earned by a T-shirt factory is modeled by p(x) = −x² + 1400x − 80,000. What range of prices will yield a profit of at least Birr 400,000?", [("600 ≤ x ≤ 800", True), ("x ≤ 800", False), ("x ≤ 600 or x ≥ 800", False), ("x ≤ 600", False)]),
]

seed(aptitude_entrance, aptitude_entrance_questions)




# =========================
# Physics Exam
# =========================

physics_exam = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Physics Part A",
    description="Physics practice exam — vectors, kinematics, dynamics, energy",
    duration_minutes=180,
)

physics_questions = [
    ("Vector quantities are represented by", [("magnitude and direction", True), ("direction only", False), ("magnitude only", False), ("dimensionless values", False)]),
    ("Two displacement vectors have magnitudes 4 m and 3 m. Which one of the following is NOT a possible value of the magnitude of their resultant?", [("1 m", False), ("7 m", False), ("5 m", False), ("12 m", True)]),
    ("Which of the following correctly describes the difference between distance and displacement?", [("Distance can be described by magnitude and direction, while displacement is described by magnitude only", False), ("Distance depends on the initial and final points, while displacement depends on the path", False), ("Distance is always ≥ the magnitude of displacement, while displacement is always ≤ distance", True), ("Distance has positive or negative values, while displacement has only positive value", False)]),
    ("Given the displacement vector Ā = (3î − 4ĵ) m, what is the unit vector in the direction of Ā?", [("0.6î + 0.8ĵ", False), ("0.8î − 0.6ĵ", False), ("0.6î − 0.8ĵ", True), ("−0.6î + 0.8ĵ", False)]),
    ("If two vectors ā and b̄ form an angle α between them, the expression ab cosα defines the value of", [("scalar product of ā and b̄", True), ("resultant of ā and b̄", False), ("projection of ā on b̄", False), ("vector product of ā and b̄", False)]),
    ("You are given F₁ = 75 N (53° W of N) and F₂ = 100 N (37° E of N). Using graphical scale 1 cm = 10 N, what is the length and direction of the resultant?", [("1.73 cm to 45° North of East", False), ("1.25 cm to the North", False), ("17.3 cm to 45° North of East", False), ("12.5 cm to the North", True)]),
    ("Which pair of vectors is collinear?", [("C = î + ĵ and D = î − ĵ", False), ("A = 2î + 3ĵ and B = −4î + 6ĵ", False), ("E = −î + ĵ and F = 3î − 3ĵ", True), ("G = 2î + 3ĵ and F = 3î + 2ĵ", False)]),
    ("A person walked 10 m at 53° N of E, 10 m North, and 20 m at 37° N of W. The magnitude of the person's displacement is", [("30.0 m", False), ("31.6 m", True), ("40.0 m", False), ("20.0 m", False)]),
    ("According to Newton's first law, an object in motion continues its state of motion with", [("a decreasing speed if the resultant force on it is zero", False), ("constant velocity if the resultant force on it is not zero", False), ("an increasing speed if the resultant force on it is not zero", False), ("constant velocity if the resultant force on it is zero", True)]),
    ("Which of the following correctly describes uniformly accelerated motion?", [("The velocity is constant", False), ("The acceleration is constant", True), ("The speed is constant but the direction is changing", False), ("The displacement increases at a uniform rate", False)]),
    ("A train moving with constant acceleration of 5 m/s² passes a traffic light with velocity such that it reaches 30 m/s in 4 seconds. What is the distance from the traffic light after 8 seconds?", [("80 m", False), ("160 m", False), ("240 m", True), ("320 m", False)]),
    ("An object moving with constant acceleration a travels displacement s in time t, with initial velocity vᵢ and final velocity vf. Which relation is correct?", [("s = ((vf − vᵢ)/2) × t", False), ("s = vᵢt + ½at", False), ("s = (vf² − vᵢ²)/a", False), ("s = vft − ½at²", True)]),
    ("A ball is thrown vertically upward, reaches a maximum height, then returns. Which statement about energy and work is correct?", [("On the way up, work done by gravity is positive", False), ("On the way up, change in kinetic energy is positive", False), ("On the way down, work done by gravity is positive", True), ("On the way down, change in potential energy is positive", False)]),
    ("The velocity-time graph shows motion in a straight line. What is the magnitude of total displacement in 14 seconds? (Graph: −3 m/s for 0–2s, increasing to 12 m/s at 8s, constant to 10s, decreasing to 0 at 14s)", [("102 m", False), ("90 m", False), ("54 m", False), ("42 m", True)]),
    ("A ball thrown vertically upward with 12 m/s. Its speed when 4.0 m above the ground is", [("8 m/s", True), ("15 m/s", False), ("10 m/s", False), ("12 m/s", False)]),
    ("Suppose a ball is thrown horizontally from a building of height h with initial speed v₀. Which statement is correct about the motion?", [("Its vertical component velocity remains constant", False), ("Its horizontal component acceleration is zero", True), ("Its horizontal component velocity uniformly increases", False), ("Its vertical component acceleration is zero", False)]),
    ("A projectile is thrown from level ground with initial velocity v₀ at angle θ. If maximum height is H, what is the horizontal range in terms of H and θ?", [("R = H tanθ / 4", False), ("R = H / tanθ", False), ("R = H / (4 tanθ)", False), ("R = 4H / tanθ", True)]),
    ("An object is projected at angle θ from horizontal with velocity v₀. Which expression gives the relationship between maximum height h_max and range R?", [("R = h_max × tanθ/2", False), ("R = 4 h_max tanθ", False), ("R = 2h_max/tanθ", False), ("R = 4h_max/tanθ", True)]),
    ("A 0.5 kg block moving at 5.0 m/s slides 2.5 m on a rough surface before stopping. The coefficient of kinetic friction is", [("0.5", True), ("0.3", False), ("0.1", False), ("0.4", False)]),
    ("A 2 kg object accelerates at 1.5 m/s² to the right on a frictionless surface under two forces F₁ and F₂, where F₂ = 1 N acts to the left. What is the magnitude of F₁?", [("2 N", False), ("1 N", False), ("3 N", False), ("4 N", True)]),
    ("A particle of mass m is tied to a string and whirled in a horizontal circle. The string makes angle θ with vertical. Which force provides the centripetal force?", [("T sinθ", True), ("T cosθ", False), ("mg sinθ", False), ("mg cosθ", False)]),
    ("Block A (m₁ = 8 kg, u₁ = 6 m/s) collides with Block B (m₂ = 12 kg, u₂ = 3 m/s), both moving in +x. After collision, v₁ = 4 m/s (+x). What is v₂?", [("4.33 m/s to −x", False), ("3.71 m/s to −x", False), ("3.71 m/s to +x", False), ("4.33 m/s to +x", True)]),
    ("A tennis ball (0.10 kg) traveling at 40.0 m/s is struck by a racket and returns at 30.0 m/s in the opposite direction. The magnitude of impulse delivered to the ball is", [("3.0 kg·m/s", False), ("4.0 kg·m/s", False), ("7.0 kg·m/s", True), ("1.0 kg·m/s", False)]),
    ("A spring stores 120 J of elastic potential energy when stretched by 0.5 m. What is the potential energy stored when stretched by 1.5 m?", [("480 J", False), ("960 J", False), ("1080 J", True), ("540 J", False)]),
    ("Consider two balls A and B projected with the same velocity v₀ at angles θ₁ and θ₂ where 0 < θ₁ < 45° and 45° < θ₂ < 90°. Which statement is correct?", [("Range of ball A is less than its maximum height", False), ("Ball A takes longer than B to reach maximum height", False), ("Both balls have equal speed at their maximum heights", False), ("The two balls cover equal ranges when θ₁ + θ₂ = 90°", True)]),
    ("A car travels 60 m north and then 80 m west. The magnitude of the resultant displacement is", [("4800 m", False), ("20 m", False), ("140 m", False), ("100 m", True)]),
    ("A car initially traveling at 20 m/s decelerates at 1.5 m/s². The radius of each tire is 0.3 m. How many revolutions does each tire make before the car stops?", [("444.4 rev", False), ("70.77 rev", True), ("44.44 rev", False), ("133.33 rev", False)]),
    ("A wheel of radius r = 50 cm rotates with angular speed ω = 200 rad/s. What is the tangential speed of a point on the rim?", [("800 m/s", False), ("10,000 m/s", False), ("100 m/s", True), ("80,000 m/s", False)]),
    ("Which of the following statements is correct about static and dynamic equilibrium?", [("Static: object at rest; Dynamic: object moves with constant velocity", True), ("Static: object moves with constant acceleration; Dynamic: object is at rest", False), ("Static: acceleration = 0; Dynamic: acceleration increases uniformly", False), ("Static: object moves with constant velocity; Dynamic: object is at rest", False)]),
    ("Which one of the following is a necessary condition for an object to be in linear equilibrium?", [("The net force acting on the object is a non-zero constant", False), ("The linear acceleration of the object is zero", True), ("The linear speed of the object is constant", False), ("The linear acceleration of the object is a non-zero constant", False)]),
]

seed(physics_exam, physics_questions)