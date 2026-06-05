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
    ("Which one of the following CORRECTLY shows the relative charges of an electron, proton and neutron, respectively?", [("0, +1, -1", False), ("0, -1, +1", False), ("-1, +1, 0", False), ("-1, 0, +1", True)]),
    ("Which statement below CORRECTLY describes the Bohr's model of an atom?", [("Protons and electrons are found in the nucleus", False), ("Electrons and neutrons are found in the nucleus", False), ("Protons move in circular orbits around the nucleus", False), ("Electrons move in circular orbits around the nucleus", True)]),
    ("Which statement below CORRECTLY describes periodicity? Periodicity is", [("a regular repetition of chemical and physical properties in the Periodic Table", True), ("a row in the Periodic Table which contains elements with same number of shells", False), ("a measure of electronegativity which runs from least to most electronegative elements", False), ("a column of the Periodic Table which contains elements with similar chemical properties", False)]),
    ("Which statement below CORRECTLY expresses hydrogen bonding? It is formed by bonding", [("a hydrogen atom to an element such as sodium", False), ("a hydrogen atom to an element such as oxygen", True), ("two hydrogen atoms with equal sharing of electrons", False), ("two hydrogen atoms with unequal sharing of electrons", False)]),
    ("What is the bond formed between two or more atoms by sharing of electrons?", [("Ionic bond", False), ("Metallic bond", False), ("Covalent bond", True), ("Valence bond", False)]),
    ("Which statement below CORRECTLY describes dipole-dipole forces? It is the force that exists", [("in all molecules", False), ("between polar molecules", True), ("between non-polar molecules", False), ("between polar and non-polar molecules", False)]),
    ("Comparing the forces between molecules of similar molar masses, which one of the following produces the weakest force?", [("Covalent bonds", False), ("Hydrogen bonding", False), ("Ionic forces", False), ("Van der Waals forces", True)]),
    ("What is a limiting reactant? It is the reactant that", [("regenerated at the end of the reaction", False), ("remains unreacted as the reaction proceeds", False), ("present in excess when the reaction goes to completion", False), ("completely consumed when the reaction goes to completion", True)]),
    ("Which statement below CORRECTLY distinguishes redox and non-redox reactions?", [("Electrons are transferred in redox reactions but not in non-redox reactions", True), ("Reduction occurs in redox reactions and oxidation takes place in non-redox reactions", False), ("Oxidation number remains the same in both redox and non-redox reactions", False), ("Acid-base reactions can be considered as both redox and non-redox reactions", False)]),
    ("Given the reaction C(s) + CO2(g) = 2CO(g). What is the equilibrium constant expression for the reaction?", [("[CO]^2 / [C][CO2]", False), ("[CO]^2 / [CO2]", True), ("[CO]^2 / [C]", False), ("[C][CO2] / [CO]^2", False)]),
    ("Which of the following pair of substances can be considered as examples of the liquid state of matter at room temperature and 1 atm pressure?", [("Carbon and mercury", False), ("Water and carbon dioxide", False), ("Water and mercury", True), ("Carbon and carbon monoxide", False)]),
    ("Which gas law describes the behavior of gases using the variables: temperature, volume, pressure and number of moles?", [("Ideal gas law", True), ("Boyle's law", False), ("Avogadro's law", False), ("Combined gas law", False)]),
    ("Which statement below describes CORRECTLY the assumptions in the kinetic theory of gases?", [("Gas molecules occupy a finite volume and have indefinite shape", False), ("Gas molecules are in random motion with no interactions", True), ("The average kinetic energies of gas molecules are independent of temperature", False), ("The average kinetic energies of gas molecules are independent of the amount of gas", False)]),
    ("If the rate of diffusion of a certain unknown gas is half times the rate of diffusion of helium, what will be the molar mass of the unknown gas? (Atomic mass of He = 4.0 g/mole)", [("2.0 g/mole", False), ("8.0 g/mole", False), ("16.0 g/mole", True), ("32.0 g/mole", False)]),
    ("A student added boiling chips into a beaker of water while carrying out an activity to determine the boiling point of water. Why do you think the boiling chips are necessary?", [("To ensure smooth rate of evaporation", True), ("To speed up the rate of evaporation", False), ("To maintain constant temperature and pressure", False), ("To reach the boiling point with less consumption of heat", False)]),
    ("What is the oxidation number of manganese in KMnO4? (Atomic Number K=19, Mn=25 and O=16)", [("+5", False), ("+6", False), ("+7", True), ("+8", False)]),
    ("Aluminum reacts with oxygen to form aluminum oxide. What is the coefficient of aluminum after balancing the reaction? (Atomic number of Al=13, O=16)", [("2", False), ("4", True), ("6", False), ("8", False)]),
    ("What property of an ionic compound can be investigated by heating it in a crucible?", [("Melting point", True), ("Solubility", False), ("Malleability", False), ("Crystallization point", False)]),
    ("Silver has two known isotopes, 107Ag and 108Ag with their percent abundance of 52% and 48% respectively. What is the average atomic mass of silver?", [("107.89", False), ("108.06", False), ("107.48", True), ("108.86", False)]),
    ("Which reaction scheme below illustrates the formation of a cation?", [("Na -> Na+ + e-", True), ("2Cl- -> Cl2 + 2e-", False), ("S + 2e- -> S2-", False), ("Mg2+ + 2e- -> Mg", False)]),
    ("Which law governs the fact that the ratio of the amount of hydrogen to oxygen by weight will be the same in a drop of water and a lake of water?", [("Law of relative composition", False), ("Law of conservation of mass", False), ("Law of multiple proportions", False), ("Law of definite composition", True)]),
    ("Which statement below CORRECTLY describes the characteristics of chemical equilibrium?", [("A reaction stops when it reaches equilibrium", False), ("A reaction stops if sufficient amount of time is given", False), ("The rates of the forward and reverse reactions are equal", True), ("A new substance or substances are formed when equilibrium is attained", False)]),
    ("What is the CORRECT IUPAC nomenclature of the alkane with CH3 at C2, CH3 at C9, Cl at C4 and C6 on a 10-carbon chain?", [("5,7-dichloro-3,9-dimethyldecane", False), ("4,6-dichloro-2,8-dimethyldecane", True), ("4,6-dichloro-2-ethyl-8-methylnonane", False), ("4,6-dichloro-8-ethyl-2-methylnonane", False)]),
    ("What is the name given to compounds of carbon and hydrogen containing multiple bonds?", [("Aliphatic hydrocarbons", False), ("Aromatic hydrocarbons", False), ("Saturated hydrocarbons", False), ("Unsaturated hydrocarbons", True)]),
    ("2-methyl-1-butene is one of the isomers of C5H10. Which of the following is the CORRECT structural formula of this isomer?", [("CH3-CH(CH3)-CH=CH2", True), ("CH3-CH2-C(CH3)=CH2", False), ("CH3-C(CH3)=CH-CH3", False), ("CH3-CH=CH-CH2-CH3", False)]),
    ("Which of the following organic compounds is used for the production of 1,2-ethanediol?", [("Ethene", True), ("Ethane", False), ("Ethyne", False), ("Ethanol", False)]),
    ("Which of the following is the main constituent of natural gas?", [("Ethane", False), ("Butane", False), ("Propane", False), ("Methane", True)]),
    ("In order to avoid the decrease in quality of some clothes after washing with water, which of the following chemicals is used for dry cleaning?", [("CH4", False), ("CH2Cl2", False), ("C2H4", False), ("C2Cl4", True)]),
    ("Which of the following properties is the property of an acidic oxide? An acidic oxide reacts with", [("salts to form acids", False), ("water to form acids", True), ("bases to form basic hydroxide and water", False), ("basic oxides to form hydroxides and water", False)]),
    ("What is the name given to an acid that dissociates (ionizes) only to a slight extent in aqueous solution?", [("Dilute acid", False), ("Strong acid", False), ("Weak acid", True), ("Concentrated acid", False)]),
    ("Solutions can be classified based upon their pH values. What is a solution whose pH value is 13?", [("Amphoteric solution", False), ("Acidic solution", False), ("Neutral solution", False), ("Basic solution", True)]),
    ("During laboratory class, a student placed clean water in a beaker and added pieces of calcium metal using tongs. After the reaction is completed, he/she tested the solution using red litmus paper. Which of the following will be observed?", [("The litmus paper turns to blue", True), ("The litmus paper turns to red", False), ("The litmus paper maintains its color", False), ("The litmus paper turns to colorless", False)]),
    ("In an activity during laboratory session a small amount of lead bromide (PbBr2) crystals were placed in a beaker. Two electrodes are inserted until they are in contact with the PbBr2 crystals. When the PbBr2 crystals in the beaker are gently heated, which of the following will be observed?", [("Bromine gas is evolved at the anode", True), ("Bromide ion is oxidized at the cathode", False), ("Lead (II) ion is reduced at the anode", False), ("Lead (II) ion is oxidized at the cathode", False)]),
    ("What is the name given to the pollution caused by the dumping of non-biodegradable wastes into the environment?", [("Air pollution", False), ("Land pollution", True), ("Sound pollution", False), ("Water pollution", False)]),
    ("What is the purpose of the conversion of pig iron to steel?", [("To remove impurities by oxidation", True), ("To remove impurities by reduction", False), ("To increase the concentration of iron in the pig iron", False), ("To decrease the concentration of iron in the pig iron", False)]),
    ("Which of the following statements CORRECTLY describes the law of conservation of mass?", [("The total mass of substances varies during a chemical reaction", False), ("Mass is neither created nor destroyed during a chemical reaction", True), ("A particular compound is composed of the same elements in the same parts by mass", False), ("Pure compounds always contain the elements in the same percentage by mass", False)]),
    ("A mineral absorbs purple light of frequency 7.11 x 10^14 Hz. What is the wavelength (in nm) of the absorbed light? (C = 3.00 x 10^8 m/s)", [("184.4 nm", False), ("237.5 nm", False), ("421.9 nm", True), ("514.5 nm", False)]),
    ("Why do atoms absorb energy when their electrons undergo transitions from a lower energy to a higher energy level? This is because", [("the electrons of the atoms move from one orbit of lower radius to another one having larger radius", True), ("the electrons of the atoms move from one orbit of higher radius to another one having lower radius", False), ("the electrons of the atoms do not have allowable energy levels", False), ("electrons of the atoms absorb energy when they go from higher to lower energy", False)]),
    ("What are the quantum numbers for the 5s orbital?", [("n=5, l=0, ml=-1, ms=+/-1/2", False), ("n=5, l=1, ml=-2, ms=+/-1/2", False), ("n=5, l=2, ml=-2, ms=+/-1/2", False), ("n=5, l=0, ml=0, ms=+/-1/2", True)]),
    ("Which of the following is CORRECT about the set of quantum numbers assigned to the two electrons of the helium atom?", [("Both electrons have the same four quantum numbers", False), ("The second electron occupies the same orbital as the first with the same spin quantum number", False), ("The second electron occupies the same orbital as the first with the opposite spin quantum number", True), ("The magnetic quantum numbers of both electrons are different", False)]),
    ("Scandium (Sc) has the electron configuration [Ar] 4s^2 3d^1. To which group of elements does it belong to?", [("Representative elements", False), ("Transition elements", True), ("Inner transition elements", False), ("Nonmetals", False)]),
    ("A student carried out an experiment to determine the melting points of NaCl and CuCl2. He/she added 0.2 g of NaCl and CuCl2 into two different test tubes and heated both tubes simultaneously using a Bunsen burner. Which of the following statements is CORRECT regarding the melting point of NaCl and CuCl2?", [("The melting points of NaCl are lower than that of CuCl2", False), ("The melting point of NaCl is higher than that of CuCl2", True), ("Both NaCl and CuCl2 will start to melt at the same time", False), ("Both NaCl and CuCl2 will not melt", False)]),
    ("The molecule COCl2 (phosgene) has a trigonal planar geometry. What is the Cl-C-Cl bond angle relative to 120 degrees?", [("Equal to 120 degrees", False), ("Greater than 120 degrees", False), ("Slightly less than 120 degrees", True), ("90 degrees", False)]),
    ("What is the cause of unusual high boiling points of HF, H2O and NH3?", [("Dipole-Dipole forces", False), ("Induced dipole forces", False), ("Hydrogen bonding", True), ("Ion-dipole forces", False)]),
    ("Which one of the following CORRECTLY illustrates the hybridization of orbitals of Be in the molecule BeCl2?", [("sp3 hybridization with 4 hybrid orbitals", False), ("sp3 hybridization with lone pairs", False), ("sp hybridization: one 2s and one 2p combine to form two sp orbitals", True), ("sp2 hybridization with three hybrid orbitals", False)]),
    # FIXED: all four answer options are now distinct
    ("What is the electron configuration of O2- molecule as per the molecular orbital model? (Atomic number of O = 8)", [
        ("sigma1s2 sigma*1s2 sigma2s2 sigma*2s2 sigma2px2 pi2py2 pi2pz2 pi*2py1 pi*2pz0", False),
        ("sigma1s2 sigma*1s2 sigma2s2 sigma*2s2 sigma2px2 pi2py2 pi2pz2 pi*2py2 pi*2pz1", True),
        ("sigma1s2 sigma*1s2 sigma2s2 sigma*2s2 sigma2px2 pi2py2 pi2pz2 pi*2py1 pi*2pz1", False),
        ("sigma1s2 sigma*1s2 sigma2s2 sigma*2s2 sigma2px2 pi2py1 pi2pz2 pi*2py2 pi*2pz1", False),
    ]),
    ("Which of the following factors does NOT affect the rate of a chemical reaction having solid reactants?", [("Concentration of reactants", False), ("Temperature of reaction", False), ("Physical state of reactants", False), ("Volume of reaction vessel", True)]),
    ("At a particular temperature, the equilibrium constant Kc = 0.36 for the reaction SO3(g) = SO2(g) + O2(g). In an experiment, 1.00 mol of SO3 is introduced into a 1.00 L container. It was found that there is 0.50 mol of SO2 at equilibrium in the same volume. Which of the following predictions can be drawn from the given data?", [("The reaction is at equilibrium", False), ("The reaction will proceed to the left", False), ("The reaction will proceed to the right", True), ("It is not possible to predict the direction of the reaction", False)]),
    ("What is the density of methane (CH4) at a pressure of 900 torr and a temperature of 25 degrees C? (R = 0.082 atm L/mol K, 1 atm = 760 torr)", [("0.78 g/L", False), ("0.92 g/L", False), ("1.25 g/L", True), ("9.2 g/L", False)]),
    ("It takes 2.25 minutes for 0.02 mol of He to diffuse. How long will it take to diffuse for the same amount of methane gas, CH4? (M.wt of He = 4 g/mol, CH4 = 16 g/mol)", [("1.25 min", False), ("2.25 min", False), ("4.5 min", True), ("6 min", False)]),
    ("Which one of the following statement CORRECTLY defines rate of reaction? The rate of a reaction is", [("the changes in concentration of reactants or products per unit time", True), ("the measure of the amount of energy change in a chemical reaction", False), ("the study of necessary mechanisms occurred in a chemical reaction", False), ("the measure of the rate of diffusion of different gases inside a tube", False)]),
    ("Consider the following gaseous reversible reaction is at a state of equilibrium: PCl3(g) + Cl2(g) = PCl5(g). Which of the following changes in concentration will cause the equilibrium shift to the right?", [("Decreasing the concentrations of the reactants and products equivalently", False), ("Increasing the concentration of the reactants and products equivalently", False), ("Increasing the concentrations of the reactants and decreasing the concentration of the product", True), ("Decreasing the concentrations of the reactants and increasing the concentration of the product", False)]),
    ("Consider the following equilibrium reaction at 298 K: 2NO2(g) = 2NO(g) + O2(g). PNO2 = 0.75 atm, PNO = 2.5 x 10^-5 atm, PO2 = 3.5 x 10^-5 atm. What is the equilibrium constant (Kp) at this temperature?", [("5.2 x 10^-15", False), ("1.16 x 10^-9", False), ("2.9 x 10^-14", False), ("3.9 x 10^-14", True)]),
    ("The molecule of BrF5 has both bonding and lone pair of electrons. Based upon these electrons, which one is the CORRECT molecular geometry of the molecule of BrF5?", [("Square planar", False), ("Square pyramidal", True), ("Trigonal pyramidal", False), ("Trigonal bipyramidal", False)]),
    ("Consider the structure of an alcohol: CH3CH(OH)CH2CH(OH)CH3. What type of an alcohol is it?", [("Tertiary alcohol", False), ("Polyhydric alcohol", False), ("Primary alcohol", False), ("Dihydric alcohol", True)]),
    ("What is the IUPAC name of the carboxylic acid: HOC-CH2-CH(Cl)-CH2-CH2-CH2-CH2-COH (with two COOH groups and Cl at C3)?", [("5-chlorooctanoic acid", False), ("3-chlorooctanedioic acid", True), ("2-chlorooctanedioic acid", False), ("3-chlorooctanoic acid", False)]),
    ("Which of the following statements CORRECTLY describes the relationship among wavelength, frequency and speed in an electromagnetic radiation?", [("As the wavelength increases, the frequency increases", False), ("As the wavelength decreases, the frequency increases", True), ("As the wavelength decreases, the speed of light increases", False), ("As the frequency increases, the speed of light decreases", False)]),
    ("Which of the following organic compounds has the highest boiling point?", [("Ethanol", True), ("Ethene", False), ("Ethanal", False), ("Ethane", False)]),
    ("What is a Lewis base? It is", [("proton donor", False), ("proton acceptor", False), ("electron pair acceptor", False), ("electron pair donor", True)]),
    ("Given the following information: CH3COOH(aq) = CH3COO-(aq) + H+(aq), Initial concentration 0.2 M. Which of the following expression represent for the percent ionization of CH3COOH?", [("(x / (0.2 - x)) x 100%", False), ("(x / 0.2) x 100%", True), ("((0.2 - x) / 0.2) x 100%", False), ("(0.2 / x) x 100%", False)]),
    ("Which statement distinguishes equivalence point from end point in acid base titration?", [("Equivalence point is where reactants start to evaporate; end point is where a product starts to condense", False), ("Equivalence point is where reactants start to melt; end point is where products start to freeze", False), ("Equivalence point is where the indicator changes color; end point is where an acid has completely reacted with a base", False), ("End point is where the indicator changes color; equivalence point is where an acid has completely reacted with a base", True)]),
    ("Which one is the mathematical expression for Faraday's first law of electrolysis?", [("m1/E1 = m2/E2", False), ("M = n/V(liter)", False), ("m = MPV/RT", False), ("m = MIt/nF", True)]),
    ("Which of the following describes the process of manufacturing valuable products in industries?", [("Designing to produce a desired output from raw materials using energy through different steps", True), ("Discharging of a solid, liquid or gaseous substance into an environment that causes unwanted changes", False), ("Carry out unwanted reaction of a material that result in the dissolution or consumption of the material", False), ("Manufacturing industry uses only organic chemicals in the production of valuable products", False)]),
    ("Which of the following reaction shows the action of H2SO4 as oxidizing agent?", [("SO3(g) + H2O(l) -> H2SO4(aq)", False), ("2KOH(aq) + H2SO4(aq) -> K2SO4(aq) + 2H2O(l)", False), ("Cu(s) + 2H2SO4(aq) -> CuSO4(aq) + SO2(g) + H2O(l)", True), ("Mg3N2(s) + 4H2SO4(aq) -> 3MgSO4(aq) + (NH4)2SO4(aq)", False)]),
    ("Which type of glass is made by heating a mixture of silica, sodium carbonate and limestone?", [("Quartz", False), ("Borosilicate", False), ("Pyrex", False), ("Soda-lime", True)]),
    ("Consider the following galvanic cell with a Zinc strip in 1.0 M Zn(NO3)2 connected to Metal B in 1.0 M BSO4. The cell potential reads 0.51 V at 25 degrees C. What is the standard reduction potential of metal B? (E(Zn2+/Zn) = -0.76 V)", [("E(B2+/B) = -0.25 V", False), ("E(B2+/B) = -1.27 V", False), ("E(B2+/B) = +0.25 V", False), ("E(B2+/B) = +1.27 V", True)]),
    ("Which of the following polymer is used to make ropes, clothes, hair combs and stockings?", [("Perspex", False), ("Nylon", True), ("Teflon", False), ("Bakelite", False)]),
    ("Which of the following catalyst is used in the Ostwald process for the production of HNO3?", [("Pt", True), ("V2O5", False), ("Fe", False), ("CuO", False)]),
    ("In which of the following component of the environment does photosynthesis take place?", [("Atmosphere", False), ("Hydrosphere", False), ("Lithosphere", False), ("Biosphere", True)]),
    ("Which of the following is NOT true about greenhouse effect and greenhouse gases?", [("Greenhouse effect is the trapping of the infrared radiation by certain gases in the atmosphere", False), ("Carbon dioxide and water vapor are greenhouse gases", False), ("Oxygen (O2) and nitrogen (N2) are transparent to infrared radiation", False), ("The greater the percentage of greenhouse gases in the atmosphere, the cooler the earth should be", True)]),
    ("In which of the following is the type of natural resource and the given example CORRECTLY paired?", [("Renewable resources; copper", False), ("Renewable resources; crops", True), ("Non-Renewable Resources; animal wool", False), ("Non-Renewable Resources; water", False)]),
    ("Which of the following compound is a Bronsted-Lowry base?", [("BF3", False), ("NH3", True), ("HCl", False), ("H2S", False)]),
    ("For the dissociation of HNO2: HNO2(aq) = NO2-(aq) + H+(aq). What is the percent ionization of a 0.5 M solution of HNO2? (Ka of HNO2 = 7.1 x 10^-4)", [("0.2%", False), ("1.8%", False), ("3.8%", True), ("9.1%", False)]),
    ("A 0.47 M aqueous solution of a weak base has a pOH of 2. What is Kb for the weak base?", [("2.17 x 10^-4", True), ("3.14 x 10^-3", False), ("1.0 x 10^-2", False), ("4.4 x 10^-1", False)]),
    ("A student was given a standard Zn(s)/Zn2+(aq) half-cell and another half-cell containing copper immersed in 1.00 M CuSO4(aq). When the Zn was connected as the anode at 25 degrees C, the cell potential reading on the voltmeter shows 1.1 V. Which of the following is NOT correct regarding the cell potential measurement?", [("The mass of copper was increased during the cell potential measurement", False), ("The circuit is completed inside the cell by migration of ions through the salt bridge", False), ("The zinc electrode was dissolved and the blue color CuSO4 solution would fade", False), ("Electrons travel through the external circuit from copper cathode to the zinc anode", True)]),
    ("Which of the following polymer structure represents polypropylene?", [("Polyethylene structure with only H substituents", False), ("Polyvinyl chloride structure with Cl substituents", False), ("Structure with alternating H and CH3 substituents on carbon backbone", True), ("Structure with CH3 and COOCH3 substituents", False)]),
    ("The following reaction can be used for the synthesis of CH3CH=CHCH3: CH3CH2CHBrCH3 + CH3S- -> CH3CH=CHCH3 + CH3SH + Br-. Which of the following is the atom economy for the above reaction? (Atomic masses: H=1, C=12, S=32 and Br=80)", [("30.43%", False), ("48%", False), ("56%", True), ("80%", False)]),
    ("Which of the following process involves preventing the growth of bacteria, fungi and reducing the oxidation of fats?", [("Haber-Bosch process", False), ("Tanning", False), ("Food preservation", True), ("Contact process", False)]),
    ("Which of the following is the overall reaction for electrolysis of molten NaCl?", [("Na(l) + 1/2 Cl2(g) -> Na+(l) + Cl-(l)", False), ("Na+(l) + Cl-(l) -> Na(l) + 1/2 Cl2(g)", True), ("H2(g) + 1/2 O2(g) -> H2O(g)", False), ("H2O(g) -> H2(g) + 1/2 O2(g)", False)]),
    ("Which of the following occur during the electrolysis of dilute H2SO4?", [("SO4 2- is discharged at the anode", False), ("The overall reaction is: H2(g) + 1/2 O2(g) -> H2O(g)", False), ("H+ is discharged at the negative electrode", True), ("A basic solution is formed", False)]),
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