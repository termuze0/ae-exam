from exams.models import Exam, Question, Answer
chemistry_questions_2016 = [
    ("What are the molecular formulae of an alkene and alkyne containing seven carbon atoms, respectively?", [("C7H14 and C7H12", True), ("C7H16 and C7H14", False), ("C7H14 and C7H16", False), ("C3H12 and C7H14", False)]),
    ("Which of the following is the CORRECT method of preparation of alkenes in the laboratory?", [("Alkylation of sodium acetylide with a primary alkyl halide.", False), ("Heating of sodium salt of an organic acid with soda lime.", False), ("Reaction of halogenated alkane with sodium.", False), ("Dehydration of alcohols with concentrated sulfuric acid.", True)]),
    ("Which of the following is the CORRECT structure of benzene?", [("Hexagon with an alternating arrangement of three single and three double bonds (or a central ring)", True), ("Hexagon with only one double bond", False), ("Hexane ring without double bonds", False), ("Pentagon ring", False)]),
    ("Which of the following is the product of fractional distillation of crude oil?", [("Producer gas", False), ("Naphthalene", False), ("Water gas", False), ("Kerosene", True)]),
    ("What is the molecular formula and IUPAC name of a saturated monocarboxylic acid having six carbon atoms?", [("C5H11COOH, heptanoic acid", False), ("C6H13COOH, heptanoic acid", False), ("C5H11COOH, hexanoic acid", True), ("C6H13COOH, hexanoic acid", False)]),
    ("Given the structure CH3-O-CH3 (or CH3-CH2-O-CH3/similar structure denoted in graphic), for the ether representation shown:", [("Methyl ethanoate", False), ("Ethyl ethanoate", False), ("Propyl formate", False), ("Ethyl acetate (or structural equivalent)", True)]),
    ("During summer, the average value for the temperature measured in a certain chemistry laboratory is 298.15 K. How many decimal places are there in the measured value?", [("5", False), ("3", False), ("2", True), ("1", False)]),
    ("Which of the following is the CORRECT Lewis electron - dot symbol of MgO? (Atomic number: Mg=12 and O=8)", [("Mg+ :O: 2-", False), ("Mg+2 :O: 2-", True), ("Mg+ :O:", False), ("Mg+2 :O:", False)]),
    ("A student collected four beakers in his/her laboratory and added some small amounts of the following: naphthalene to the first, graphite to the second, iodine to the third and alcohol to the fourth. If they added equal volume of water to each of the above beakers and shake each beaker, which of the following will be their observation?", [("There will be dissolution in the first three beakers.", False), ("Water will dissolve iodine rather than graphite.", False), ("Water will dissolve the whole given chemicals in the four beakers.", False), ("There will be dissolution of alcohol in the fourth beaker.", True)]),
    ("Which of the following explanations about reversible and irreversible reactions is CORRECT?", [("A reaction that has only a forward reaction or a reverse reaction is known as a reversible chemical reaction.", False), ("A reaction that proceeds from reactant to product and from product to reactant is known as an irreversible reaction.", False), ("Chemical reactions that proceed only towards the formation of a product are known as irreversible reactions.", True), ("Chemical reactions that proceed only towards the formation of a product are known as reversible reactions.", False)]),
    ("Consider the following three steps: Step 1: Electrolysis of water and fractional distillation of air; Step 2: Passing hot mixture of gases through a condenser; Step 3: Introducing hydrogen and nitrogen gases in a chamber containing iron particles at a temperature of 300 - 500 °C and a pressure of 15 - 25 MPa. Which of the following is the CORRECT sequence involved during the industrial production of ammonia using the Haber process?", [("Step 1 -> Step 3 -> Step 2", True), ("Step 2 -> Step 3 -> Step 1", False), ("Step 2 -> Step 1 -> Step 3", False), ("Step 1 -> Step 2 -> Step 3", False)]),
    ("Which of the following is a physical property of nitric acid, HNO3?", [("On exposure to light, it turns brown.", False), ("Nitric acid is a corrosive chemical.", False), ("Nitric acid has a pungent smell.", True), ("It forms large number of salts.", False)]),
    ("Which of the following is the CORRECT explanation about herbicides?", [("Selective herbicides control specific weed species, leaving the desired crop unharmed.", True), ("Organochlorine compounds are the most common herbicide substances.", False), ("Herbicides are substances that are used to control unwanted insects.", False), ("Herbicides are substances that are used to enhance the growth of important plants.", False)]),
    ("A student collected information on the preparation of the local alcoholic drink 'ARAKI' involving Step 1 (Distillation), Step 2 (Liquefying dough & fermenting), Step 3 (Bikel & starter preparation), Step 4 (Baking bread, mixing with starter & fermenting). Which of the following is the correct procedure for the preparation of Araki?", [("Step-2 -> Step-4 -> Step-3 -> Step-1", False), ("Step-2 -> Step-3 -> Step-4 -> Step-1", False), ("Step-3 -> Step-4 -> Step-2 -> Step-1", True), ("Step-4 -> Step-3 -> Step-2 -> Step-1", False)]),
    ("Which one of the following synthetic polymers is used to make squeeze bottles, plastic wrapping and electrical insulation?", [("Polypropylene", False), ("Polyvinylchloride", False), ("Polyethylene", True), ("Polymethyl methacrylate", False)]),
    ("Which of the following descriptions of the property of a covalent compound is CORRECT?", [("Covalent compounds have low melting and boiling points.", True), ("Most covalent compounds are solids at room temperature.", False), ("Most covalent compounds are soluble in water.", False), ("Covalent compounds are non-volatile.", False)]),
    ("The attractive force between molecules is known as", [("nuclear force", False), ("intermolecular force", True), ("lattice force", False), ("intramolecular forces", False)]),
    ("The hybridization of the central atom xenon (Xe) in xenon tetrafluoride, XeF4, is sp3d2. Which of the following is the shape of XeF4?", [("Octahedral", False), ("Square planar", True), ("Tetrahedral", False), ("Seesaw shape", False)]),
    ("Which of the following is the CORRECT electron configuration of a peroxide ion, O2^2-?", [("(sigma_1s)^2(sigma*_1s)^2(sigma_2s)^2(sigma*_2s)^2(sigma_2px)^2(pi_2py^2=pi_2pz^2)(pi*_2py^2=pi*_2pz^2)", True), ("Alternative B config", False), ("Alternative C config", False), ("Alternative D config", False)]),
    ("Consider the reaction: N2(g) + O2(g) -> 2NO(g). If the rate of disappearance of N2 is 2.5 * 10^-6 M/s, what is the rate of reaction for the formation of NO?", [("5.0 * 10^-6 M/s", True), ("1.25 * 10^-3 M/s", False), ("2.50 * 10^-3 M/s", False), ("2.50 * 10^-6 M/s", False)]),
    ("Which of the following is a Lewis acid?", [("SO4^2-", False), ("SO3^2-", False), ("BF3", True), ("NH3", False)]),
    ("The pH of a 0.10 M solution of an aqueous solution of a certain acid is 3. What is the value of acid ionization constant (Ka) of this acid?", [("1.0 * 10^-7", False), ("1.0 * 10^-5", True), ("1.0 * 10^-3", False), ("1.0 * 10^-1", False)]),
    ("The shift in the position of equilibrium caused by the addition of an ion already involved in the reaction is known as", [("common ion effect", True), ("buffer ion effect", False), ("hydrolysis - effect", False), ("titration - effect", False)]),
    ("Which of the following is CORRECT about equivalents of acids and bases?", [("The volume of an acid or base required to reach equivalence point during acid - base titration reaction.", False), ("The number of moles of an acid or base required to form a one molar aqueous acidic or basic solution.", False), ("It is the amount of a substance that is required to react with one mole of hydroxide ions in redox reactions.", False), ("It is the amount of a substance that is required to react with one mole of hydrogen ions in acid - base reactions.", True)]),
    ("A 250 mL solution is formed from 24.5 g of sulfuric acid (H2SO4). What is the normality of this solution? (Mol. wt. H2SO4 = 98 g/mol)", [("4.00 N", False), ("2.00 N", True), ("0.250 N", False), ("0.125 N", False)]),
    ("Which of the following reaction is used for the preparation of bases?", [("Reaction of metal hydroxides with dilute acids.", False), ("Reaction of active metal oxides with water.", True), ("Heating of a salt with a non - volatile acid.", False), ("Heating of carbonates with dilute acids.", False)]),
    ("Which of the following salts is used in the treatment of waste water?", [("CaCO3", False), ("BaSO4", False), ("FeCl3", True), ("KNO3", False)]),
    ("A student dissolved 10 mL of concentrated HCl in the first beaker and 10 mL of concentrated CH3COOH in the second beaker containing water. Which of the following would occur in the solution?", [("In the first beaker, a large fraction of HCl dissociates into ions and in the second beaker, a small fraction of CH3COOH dissociates into ions.", True), ("In the first beaker, a small fraction of HCl dissociates into ions and in the second beaker, a large fraction of CH3COOH dissociates into ions.", False), ("There is no dissociation or ionization of the HCl and CH3COOH in both the first and second beakers.", False), ("The amount of HCl dissociated in the first beaker and the amount of CH3COOH dissociated in the second beaker are identical.", False)]),
    ("Consider the steps during the extraction of aluminum from its bauxite ore by the Hall process: I. Treating mixture with acid, II. Heating aluminum oxide strongly, III. Heating ore with NaOH, IV. Conversion to soluble sodium aluminate, V. Electrolysis of molten mixture. Which of the following is the CORRECT sequence of production?", [("III, IV, I, II and V", True), ("IV, II, I, III and V", False), ("V, I, II, IV and III", False), ("II, I, III, IV and V", False)]),
    ("Which of the following food preservation methods leaves a product without loss of aroma or flavor?", [("Vacuum - packing", False), ("Freeze - drying", True), ("Freezing", False), ("Melting", False)]),
    ("The electronic configuration of an element in the periodic table is 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5. Which block does this element belong?", [("f-block", False), ("d-block", False), ("p-block", True), ("s-block", False)]),
    ("Consider the chart showing general periodic properties: 'Decreases' going across a period left-to-right, and 'Increases' going down a group. Which property CORRECTLY agrees with this trend?", [("Electronegativity", False), ("Electron affinity", False), ("Ionization energy", False), ("Atomic radius", True)]),
    ("Which of the following is CORRECT about the formation of a covalent bond? A covalent bond is formed", [("between positively and negatively charged ions.", False), ("between mobile and stationary electrons.", False), ("by the sharing of valence electrons.", True), ("by the transfer of valence electrons.", False)]),
    ("The molecule of carbon tetrachloride (CCl4) has four polar (C-Cl) bonds. However, CCl4 is a non-polar molecule. Which of the following explains the reason for the observed property of CCl4?", [("The molecule is non-polar because of the presence of four polar C-Cl bonds in the molecule.", False), ("The molecule is non-polar because of the difference in electronegativity between carbon and chlorine.", False), ("Even though the bond in CCl4 is polar, the net dipole moment of the molecule is different from zero.", False), ("Even though the bond in CCl4 is polar, the net dipole moment of the molecule is zero.", True)]),
    ("Which of the following is responsible for the unusual high boiling points of HF, H2O and NH3?", [("London dispersion forces", False), ("Hydrogen bonding", True), ("Covalent bonding", False), ("Ionic bonding", False)]),
    ("From the assumption of kinetic molecular theory of gases, which of the following is CORRECT?", [("The pressure of a gas is the effect of the negligible volume of the gas compared to the total volume of the gas", False), ("The average kinetic energy of gas particles is inversely proportional to the absolute temperature of the gas.", False), ("There are some forces of attraction or repulsion between gas particles.", False), ("Under ordinary conditions, the total volume of gas molecules is much smaller than the total volume of gas.", True)]),
    ("Which of the following is CORRECT about the phase change observed in water?", [("Water starts to evaporate at the boiling point and condenses at the melting point.", False), ("When a solid ice is heated, it is changed to liquid water without melting.", False), ("At the boiling point temperature, water exists in three different physical states.", False), ("At the melting point of ice, the temperature remains constant.", True)]),
    ("Given the symbols of the three subatomic particles: electrons (e), protons (p+) and neutrons (n0), which of the following is the CORRECT comparison of the absolute masses of protons, electrons and neutrons?", [("Mass of e > mass of p+ = mass of n", False), ("Mass of e = mass of p+ > mass of n0", False), ("Mass of e < mass of p+ < mass of n0", True), ("Mass of e > mass of p+ > mass of n0", False)])
]

chemistry_questions_deep_explanation = [
    ("Given the symbols electrons (e⁻), protons (p⁺) and neutrons (n⁰), which of the following is the CORRECT comparison of their absolute masses?", [
        ("Mass of e⁻ > mass of p⁺ = mass of n⁰", False),
        ("Mass of e⁻ = mass of p⁺ > mass of n⁰", False),
        ("Mass of e⁻ < mass of p⁺ < mass of n⁰", True),
        ("Mass of e⁻ > mass of p⁺ > mass of n⁰", False)
    ]),
    ("'The hydrogen atom moves in a fixed circular orbit associated with allowable energy states.' This statement describes which theory?", [
        ("Planck's theory", False),
        ("Bohr's theory", True),
        ("Pauli's principle", False),
        ("Aufbau's principle", False)
    ]),
    ("Which is the core electron configuration of the metal ion in ferric sulfate, Fe₂(SO₄)₃? (Atomic Number of Fe = 26)", [
        ("[Ar] 4s²3d³", False),
        ("[Ar] 4s²3d⁶", False),
        ("[Ar] 3d⁵", True),
        ("[Ar] 3d⁶", False)
    ]),
    ("An element has the electronic configuration 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁵. In which block does this element belong?", [
        ("f-block", False),
        ("d-block", False),
        ("p-block", True),
        ("s-block", False)
    ]),
    ("In the modern periodic table, which group contains the most electronegative elements?", [
        ("Alkali metals", False),
        ("Halogens", True),
        ("Chalcogens", False),
        ("Noble gases", False)
    ]),
    ("An element has atomic number 55 and mass number 133. Which CORRECTLY describes a property of this element?", [
        ("The non-metallic character of the element is high.", False),
        ("The metallic character of the element is high.", True),
        ("The element has high electron affinity.", False),
        ("The element has high electronegativity.", False)
    ]),
    ("A chart shows a property that DECREASES across a period (left→right) and INCREASES down a group. Which property matches this trend?", [
        ("Electronegativity", False),
        ("Electron affinity", False),
        ("Ionisation energy", False),
        ("Atomic radius", True)
    ]),
    ("Which of the following characteristics of electromagnetic radiation is CORRECT?", [
        ("The speed decreases with increasing wavelength.", False),
        ("The speed increases with increasing frequency.", False),
        ("The speed is independent of the medium it travels through.", True),
        ("The wavelength is directly proportional to its frequency.", False)
    ]),
    ("Which is the CORRECT Lewis electron-dot symbol of MgO? (Atomic numbers: Mg = 12, O = 8)", [
        ("Mg⁺ :O:²⁻  (4 dots on O)", False),
        ("Mg²⁺ :O:  (2 dots on O)", False),
        ("Mg⁺ :O:  (4 dots on O)", False),
        ("Mg²⁺ :O:²⁻  (4 dots on O)", True)
    ]),
    ("Which of the following is CORRECT about the formation of a covalent bond?", [
        ("Formed between positively and negatively charged ions.", False),
        ("Formed between mobile and stationary electrons.", False),
        ("Formed by the sharing of valence electrons.", True),
        ("Formed by the transfer of valence electrons.", False)
    ]),
    ("Which of the following descriptions of the property of a covalent compound is CORRECT?", [
        ("Covalent compounds have low melting and boiling points.", True),
        ("Most covalent compounds are solids at room temperature.", False),
        ("Most covalent compounds are soluble in water.", False),
        ("Covalent compounds are non-volatile.", False)
    ]),
    ("The attractive force between molecules is known as ________.", [
        ("Nuclear force", False),
        ("Intermolecular force", True),
        ("Lattice force", False),
        ("Intramolecular force", False)
    ]),
    ("Which of the following is responsible for the unusually high boiling points of HF, H₂O, and NH₃?", [
        ("London dispersion forces", False),
        ("Hydrogen bonding", True),
        ("Covalent bonding", False),
        ("Ionic bonding", False)
    ]),
    ("The hybridization of Xe in XeF₄ is sp³d². Which of the following is the shape of XeF₄?", [
        ("Octahedral", False),
        ("Square planar", True),
        ("Tetrahedral", False),
        ("Seesaw shape", False)
    ]),
    ("CCl₄ has four polar C–Cl bonds, yet CCl₄ is a non-polar molecule. Which of the following explains this?", [
        ("Non-polar because of the four polar C–Cl bonds.", False),
        ("Non-polar because of the electronegativity difference between C and Cl.", False),
        ("Even though C–Cl is polar, net dipole moment is different from zero.", False),
        ("Even though C–Cl is polar, net dipole moment of the molecule is zero.", True)
    ]),
    ("Which of the following is a Lewis acid?", [
        ("SO₄²⁻", False),
        ("SO₃²⁻", False),
        ("BF₃", True),
        ("NH₃", False)
    ]),
    ("Which is the CORRECT electron configuration of the peroxide ion, O₂²⁻?", [
        ("…(π2py²=π2pz²)(π*2py)²(σ*2z)²", False),
        ("…(π2py²=π2pz²)(π*2py²=π*2pz²)", True),
        ("…(π2py²=π2pz²)(π*2x)²", False),
        ("…(π2py=π2pz)", False)
    ]),
    ("A chemical bond that results from the attractive force between shared electrons and a nonmetal nucleus is called ________.", [
        ("Covalent bond", True),
        ("Ionic bond", False),
        ("Hydrogen bond", False),
        ("Metallic bond", False)
    ]),
    ("A water molecule has two bond pairs and two lone pairs. Which of the following is CORRECT about these pairs?", [
        ("Repulsion: bonding pair–bonding pair > lone pair–lone pair", False),
        ("Repulsion: lone pair–lone pair > bonding pair–bonding pair", True),
        ("Bonding pair–lone pair repulsion > lone pair–lone pair repulsion", False),
        ("Lone pair–lone pair repulsion = bonding pair–bonding pair repulsion", False)
    ])
]




chem_examb = Exam.objects.create(
    title="Grade 12 Ethiopian University Entrance Chemistry Part 1",
    description="Chemistry practice exam part 1",
    duration_minutes=60,
)

for question_text, choices in chemistry_questions_deep_explanation:
    q = Question.objects.create(exam=chem_examb, text=question_text)
    for choice_text, is_correct in choices:
        Answer.objects.create(question=q, text=choice_text, is_correct=is_correct)