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
    title="Grade 12 Ethiopian University Entrance Aptitude PART B",
    description="Aptitude entrance exam — verbal and quantitative reasoning",
    duration_minutes=120,
)

aptitude_entrance_questions = [
    ("Just before the time this report came out, China and India...", [("had already surpassed Europe in economic development", False), ("had become major competitors to the British economy", True), ("were still among the third world countries languishing in poverty", False), ("were growing fast but were not a threat to the European economy", False)]),
  ("We can infer from the passage that...", [("the UK has fewer highly-trained professionals in IT and engineering than other developed countries", False), ("the high demand for highly-trained personnel in IT and engineering in the UK has not been met", True), ("British people do not think a career path in IT and engineering is rewarding", False), ("British companies are employing IT and engineering professionals from elsewhere in Europe", False)]),
  ("Which one of the following statements is correct according to the report?", [("The UK will face a marked decrease in economic development", True), ("The UK is not doing anything to prevent economic decline despite warnings", False), ("The UK has managed to prevent a possible economic decline because it has plenty of experts", False), ("The probability of marked economic decline in the UK is inevitable in the face of competition", False)]),
  ("Over 20% of school leavers who complete secondary school in the UK...", [("cannot read and write", False), ("can read but are not good at writing", False), ("can read and write but not up to standard", True), ("can hardly write well because writing in English is difficult", False)]),
  ("The majority of graduate positions in British companies require...", [("effective communication skills", True), ("higher university qualifications", False), ("ability to just read and write in English", False), ("a good command of public speaking", False)]),

  ("INQUISITIVE  choose the most nearly opposite word:", [("curious", False), ("uninterested", True), ("assertive", False), ("intrusive", False)]),
  ("INDUSTRIOUS  choose the most nearly opposite word:", [("innovative", False), ("antisocial", False), ("productive", False), ("lazy", True)]),
  ("METICULOUS  choose the most nearly opposite word:", [("clueless", False), ("careless", True), ("dangerous", False), ("miraculous", False)]),

  
  ("ENDEAVOUR  choose the most nearly similar word:", [("attempt", True), ("desire", False), ("favor", False), ("despair", False)]),
  ("DECISIVE  choose the most nearly similar word:", [("important", True), ("confused", False), ("impressive", False), ("tentative", False)]),
  ("DEVASTATE  choose the most nearly similar word:", [("injure", True), ("frighten", False), ("shock", False), ("renovate", False)]),
  ("PRICELESS  choose the most nearly similar word:", [("valueless", False), ("useful", False), ("worthless", False), ("invaluable", True)]),

  
  ("LAUGHTER : DELIGHT; ________ : discontent", [("satisfaction", False), ("sorrow", True), ("excitement", False), ("complaint", False)]),
  ("DESCRIBE : PLACE; ________ : idea", [("tell", False), ("think", False), ("give", False), ("explain", True)]),
  ("APPLE : FRUIT; ________ : cereal", [("crop", False), ("wheat", True), ("orange", False), ("juice", False)]),
  ("Common : ________; SLIGHT : SEVERE", [("extraordinary", True), ("usual", False), ("expected", False), ("dull", False)]),
  ("KITCHEN : HOUSE; ________ : school", [("teacher", False), ("desk", False), ("classroom", True), ("director", False)]),

  
  ("A predator that comes to attack chickens...", [("will eat some of them and save others for future", False), ("might not have time to devour all the chickens it may find", False), ("may not be able to devour all of them as they are too many", True), ("cannot devour all of them because the mother birds will fight back", False)]),
  ("From the passage, we can infer that...", [("animals benefit from living together with their own kind", False), ("the animals described are far more intelligent", False), ("some species of apes and monkeys can recognize their aunts and uncles", False), ("lion cubs that suck at lionesses on top of their own mothers are healthier", True)]),
  ("A male frog that is a member of a larger group of frogs...", [("will definitely find a female mate", False), ("will have more than one female mate", False), ("broadens his chances of finding a female mate", True), ("has to be good at singing to find a female mate", False)]),
  ("The benefit of birds in the same colony hatching their chickens at the same time is that...", [("they can help one another in rearing them", False), ("it ensures the survival of the colony", True), ("they can share the food available to them", False), ("chickens naturally enjoy growing together", False)]),
  ("What do a group of adult elephants do to protect their young?", [("They stand in circles and keep their young in the middle", True), ("They stand in line and block the enemy from getting to their young", False), ("They aggressively charge at the enemy and scare it away", False), ("They hide their young somewhere safe, away from them", False)]),

 
  ("People flock to the capital city causing job scarcity and rising rents. What is the most logical solution?", [("The city administration should regulate entrance into the capital city", False), ("More opportunities should be created in the migrants' original areas", True), ("The city administration should create more jobs and construct more condominiums", False), ("The city administration should look for international aid to create jobs for the new arrivals", False)]),
  ("Some people with little education become multi-billionaires. We can safely conclude that...", [("formal education is a waste of time", False), ("uneducated people who become successful are always corrupt", False), ("formal education helps people to improve their talents", True), ("becoming successful in life is just a matter of chance", False)]),
  ("Five athletes raced: G/Egziabher, Haile, Kenenisa, Solomon, Sileshi. Sileshi finished before Kenenisa and Solomon but after G/Egziabher. Haile finished before Kenenisa but after Solomon. Who finished third?", [("Kenenisa", False), ("Sileshi", False), ("G/Egziabher", False), ("Solomon", True)]),
  ("Obama popular at 46 (Black American); Biden less popular at 88 (White American); Mandela popular at 88 (Black South African). Which statement is acceptable?", [("Black people make better presidents", False), ("American people are free from racism", False), ("Age and leadership quality are not necessarily interrelated", True), ("Leading America is more demanding than leading South Africa", False)]),
  ("Model A costs slightly less than B. Model C is slightly less expensive than A but its fuel consumption is higher than both A and B. Model B consumes less fuel per km than A but is not as efficient as C. Which is true?", [("Model B is the least expensive", False), ("Model C is the most expensive", False), ("Model A consumes the least fuel", False), ("Model B is the most expensive", True)]),
  ("Sara hates people who tell lies the most. Which sentence means the same?", [("Sara hates people who tell lies most of the time", False), ("What Sara hates more than anything is liars", True), ("Sara has no problem with people except liars", False), ("Sara always tells the truth", False)]),
  ("Most French people are friendly and fair. Nicola is French. I also know some French people who are biased. Therefore, Nicola...", [("may be friendly", True), ("is both friendly and fair", False), ("cannot be biased", False), ("must be fair", False)]),
  ("People in Addis Ababa speak more than one language. Zeberga was born in Adama, lived in Mekele for five years, and now lives in Addis Ababa. How many languages could Zeberga speak?", [("three", False), ("not more than two", False), ("not less than three", False), ("at least three", True)]),

 
  ("The concept of democracy is so ________ that it conveys variable meanings to different people.", [("concrete", False), ("abstract", True), ("divisive", False), ("advanced", False)]),
        ("As more people settle on areas previously inhabited by wild animals, most of such animals become ________.", [("frightened", False), ("evacuated", False), ("domesticated", False), ("endangered", True)]),
  ("Undue competition among people for natural resources will lead to ________ of land.", [("innovation", False), ("overpopulation", False), ("degradation", True), ("democratization", False)]),
  ("If you want your country to register economic development, it is ________ that you deal with corruption first.", [("imperative", True), ("arguable", False), ("possible", False), ("regrettable", False)]),
  ("Everyone respects the manager for his ________.", [("integrity", True), ("strength", False), ("charisma", False), ("elegance", False)]),


  ("Which system of linear inequalities matches the shaded region described (right, above downward-slope, below upward-slope)?", [("{ x + y ≥ 2 and −3x + 2y ≤ −6 }", True), ("{ −x + y ≥ 2 and −3x − 2y ≥ −6 }", False), ("{ −x + y ≥ 2 and −3x − 2y ≤ −6 }", False), ("{ x + y ≤ 2 and −3x + 2y ≤ −6 }", False)]),
  ("How many sheep are there if all hens and sheep in the pasture have 500 legs and 200 heads?", [("50", True), ("100", False), ("150", False), ("80", False)]),
  ("Which point is the intersection of x − y + 1 = 0 and −x − y + 2 = 0?", [("(−1/2, −3/2)", False), ("(1/2, 3/2)", True), ("(3/2, 1/2)", False), ("(−3/2, −1/2)", False)]),
  ("A school football team has grade 10, 11, and 12 students in ratio 1:2:3. If the team has 30 members, how many are grade 12?", [("20", False), ("15", True), ("10", False), ("5", False)]),
  ("Which ordered pair is in the solution set of −2x + y ≥ 0 and 3x + 2y ≤ 6?", [("(3, 1)", False), ("(1, −2)", False), ("(1, 4)", False), ("(−1, 1)", True)]),
  ("What is the coefficient of x³ in the expansion of (x³ − 20x² + 4x + 2)(15x³ + x² − 2x − 1)?", [("73", True), ("93", False), ("83", False), ("103", False)]),
  ("f(x) = x⁴ − 6x³ + 15x² − 18x + d divided by g(x) = x² − 2x + 3 gives quotient x² − bx + 4 and remainder cx − 2. What is c?", [("10", False), ("−4", False), ("4", False), ("2", True)]),
  ("A television was on 20% discount and sold for Birr 40,000. What was the original price?", [("Birr 54,000", False), ("Birr 44,000", False), ("Birr 50,000", True), ("Birr 33,000", False)]),
  ("h(t) = −5t² + 7t + 90. At what approximate time does the rock hit the ground?", [("3 seconds", False), ("4.7 seconds", False), ("6.7 seconds", False), ("5 seconds", True)]),
  ("Let f(2/3 x − 4/3) = 5x³ + 16x² + 2x + 1. Compare Quantity A = f(2) vs Quantity B = 600.", [("Quantity A is greater than Quantity B", True), ("Quantity A is less than Quantity B", False), ("The two quantities are equal", False), ("A relationship cannot be determined", False)]),
  ("Shop 1: Jan=20k, Feb=30k. Shop 2: Jan=10k, Feb=15k. Compare percentage increases.", [("Quantity A (Shop 1 increase) is greater than Quantity B", False), ("Quantity A is less than Quantity B", False), ("The two quantities are equal", True), ("The two quantities cannot be compared", False)]),
  ("What is the probability that the sum is neither 5 nor 10 when two dice are thrown?", [("2/9", False), ("7/36", False), ("7/9", False), ("29/36", True)]),
  ("4 boys and 5 girls seated alternately on 9 chairs. How many different arrangements are possible?", [("5", False), ("2,880", True), ("126", False), ("362,880", False)]),
  ("Seven students share a lined street. Given the arrangement constraints, which student lives in the other corner home?", [("S6", False), ("S3", False), ("S5", True), ("S4", False)]),
  ("Using the same street arrangement, how many homes are between S3 and S4?", [("4", False), ("2", True), ("3", False), ("1", False)]),
  ("By what approximate percent is C1's Above-50% count more than C6's Exactly-50% count?", [("49.7%", False), ("101.1%", True), ("50.3%", False), ("201.1%", False)]),
  ("What is the ratio of total students of C2 to total students scoring Exactly 50% across all countries?", [("2:3", False), ("3:2", False), ("2:1", False), ("1:2", True)]),
  ("What is the difference between the average Exactly-50% score and average Above-50% score across all countries?", [("17", True), ("144", False), ("27", False), ("244", False)]),
  ("The number of students who scored Above 50% by C4 is what percent of students who scored Below 50% by C5?", [("88.1%", False), ("50%", False), ("60%", True), ("41.1%", False)]),
  ("Which country has the least ratio of students scoring Below 50% to those scoring Above 50%?", [("C1", False), ("C3", True), ("C2", False), ("C4", False)]),
  ("Which can be the first four terms of a geometric sequence whose 4th term is 125 and 10th term is 125/64?", [("1000, 500, 250, 125, ...", True), ("1000, 500, −250, 125, ...", False), ("3375, 1125, 375, 125, ...", False), ("−500, 375, −250, 125, ...", False)]),
  ("Which term of the arithmetic sequence {24, 30, 36, 42, …} is 204?", [("30th", False), ("31st", True), ("32nd", False), ("33rd", False)]),
  ("What is the solution set of 3x − 4y = 2 and −6x + 8y = −10?", [("{(2, 1)}", False), ("{(3, 1)}", False), ("{ } (empty set)", True), ("{(0, −2)}", False)]),
  ("What is the sum of the first 16 terms of the arithmetic sequence {−2, 3/2, 5, 17/2, …}?", [("420", False), ("380", False), ("402", False), ("388", True)]),
  ("What is the value of α if Σ(n=1 to ∞) 3^(−αn) = 1/2?", [("1", True), ("−1", False), ("2", False), ("−2", False)]),
]


seed(aptitude_entrance, aptitude_entrance_questions)




