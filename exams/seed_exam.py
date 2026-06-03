from exams.models import Exam, Question, Answer

# =========================
# Physics
# =========================

physics = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Physics",
    description="Physics practice exam",
    duration_minutes=30
)

physics_questions = [
    ("What is the SI unit of force?", [("Newton", True), ("Joule", False), ("Watt", False), ("Pascal", False)]),
    ("Which law states F = ma?", [("Newton's Second Law", True), ("Newton's First Law", False), ("Ohm's Law", False), ("Hooke's Law", False)]),
    ("What is the speed of light in vacuum?", [("3×10^8 m/s", True), ("3×10^6 m/s", False), ("3×10^5 km/s", False), ("300 m/s", False)]),
    ("Which quantity is measured in Joules?", [("Energy", True), ("Force", False), ("Power", False), ("Pressure", False)]),
    ("What is acceleration due to gravity on Earth?", [("9.8 m/s²", True), ("8.9 m/s²", False), ("10.8 m/s²", False), ("12 m/s²", False)]),
    ("Which device measures electric current?", [("Ammeter", True), ("Voltmeter", False), ("Barometer", False), ("Thermometer", False)]),
    ("The unit of power is?", [("Watt", True), ("Newton", False), ("Joule", False), ("Volt", False)]),
    ("What type of lens is used in a magnifying glass?", [("Convex", True), ("Concave", False), ("Plane", False), ("Cylindrical", False)]),
    ("Which wave can travel in vacuum?", [("Light", True), ("Sound", False), ("Water", False), ("Seismic", False)]),
    ("What is the formula for density?", [("Mass/Volume", True), ("Force/Area", False), ("Distance/Time", False), ("Mass×Volume", False)]),
]

for q_text, answers in physics_questions:
    q = Question.objects.create(exam=physics, text=q_text)
    for text, correct in answers:
        Answer.objects.create(question=q, text=text, is_correct=correct)

# =========================
# Chemistry
# =========================

chemistry = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Chemistry",
    description="Chemistry practice exam",
    duration_minutes=30
)

chemistry_questions = [
    ("What is the chemical symbol for Sodium?", [("Na", True), ("So", False), ("S", False), ("N", False)]),
    ("The pH of a neutral solution is?", [("7", True), ("1", False), ("14", False), ("0", False)]),
    ("Water is composed of?", [("Hydrogen and Oxygen", True), ("Hydrogen and Nitrogen", False), ("Carbon and Oxygen", False), ("Helium and Oxygen", False)]),
    ("What is the atomic number of Carbon?", [("6", True), ("8", False), ("12", False), ("14", False)]),
    ("Which gas is used in photosynthesis?", [("Carbon Dioxide", True), ("Oxygen", False), ("Nitrogen", False), ("Hydrogen", False)]),
    ("Acids turn blue litmus paper?", [("Red", True), ("Green", False), ("Yellow", False), ("Black", False)]),
    ("What is HCl commonly called?", [("Hydrochloric Acid", True), ("Sulfuric Acid", False), ("Nitric Acid", False), ("Acetic Acid", False)]),
    ("Which particle has a positive charge?", [("Proton", True), ("Electron", False), ("Neutron", False), ("Photon", False)]),
    ("The most abundant gas in air is?", [("Nitrogen", True), ("Oxygen", False), ("Carbon Dioxide", False), ("Argon", False)]),
    ("What is the formula of table salt?", [("NaCl", True), ("KCl", False), ("HCl", False), ("CaCl", False)]),
]

for q_text, answers in chemistry_questions:
    q = Question.objects.create(exam=chemistry, text=q_text)
    for text, correct in answers:
        Answer.objects.create(question=q, text=text, is_correct=correct)

# =========================
# Biology
# =========================

biology = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Biology",
    description="Biology practice exam",
    duration_minutes=30
)

biology_questions = [
    ("What is the basic unit of life?", [("Cell", True), ("Tissue", False), ("Organ", False), ("Organism", False)]),
    ("Which organ pumps blood?", [("Heart", True), ("Lung", False), ("Kidney", False), ("Liver", False)]),
    ("Photosynthesis occurs in?", [("Chloroplast", True), ("Nucleus", False), ("Mitochondria", False), ("Ribosome", False)]),
    ("Human beings have how many chromosomes?", [("46", True), ("44", False), ("48", False), ("23", False)]),
    ("Which blood cells fight infection?", [("White Blood Cells", True), ("Red Blood Cells", False), ("Platelets", False), ("Plasma", False)]),
    ("The largest organ in the human body is?", [("Skin", True), ("Liver", False), ("Heart", False), ("Brain", False)]),
    ("Which process produces energy in cells?", [("Respiration", True), ("Photosynthesis", False), ("Digestion", False), ("Transpiration", False)]),
    ("DNA stands for?", [("Deoxyribonucleic Acid", True), ("Dynamic Nucleic Acid", False), ("Double Nitrogen Acid", False), ("None", False)]),
    ("Which kingdom does mushroom belong to?", [("Fungi", True), ("Plant", False), ("Animal", False), ("Protista", False)]),
    ("The human respiratory organ is?", [("Lung", True), ("Kidney", False), ("Heart", False), ("Liver", False)]),
]

for q_text, answers in biology_questions:
    q = Question.objects.create(exam=biology, text=q_text)
    for text, correct in answers:
        Answer.objects.create(question=q, text=text, is_correct=correct)

print("Physics, Chemistry, and Biology entrance exams created successfully.")