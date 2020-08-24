print("""
Mad Libs Generator!
1: Romeo and Juiet
2: Bee Movie
3: FitGram Pacer Test
""")

choice = int(input("Enter a number: "))
answers = []

if choice == 1:
    #                 0     1     2     3     4     5     6     7     8        9       10    11
    juliet_libs = "a name, noun, noun, noun, noun, noun, noun, noun, verb, adjective, noun, verb".title().split(", ")
    
    for x in juliet_libs:
        answers.append(input(x + ": "))

    juliet = f"""O {answers[0]}, {answers[0]}, wherefore art thou {answers[0]}?
    Deny thy {answers[1]} and refuse thy {answers[2]}.
    Or if thou wilt not, be but sworn my {answers[3]}
    And I’ll no longer be a {answers[4]}.
    ‘Tis but thy name that is my {answers[5]}:
    Thou art thyself, though not a {answers[6]}.
    What’s {answers[6]}? It is nor hand nor foot
    Nor arm nor face nor any other part
    Belonging to a man. O be some other name.
    What’s in a name? That which we call a {answers[7]}
    By any other name would {answers[8]} as {answers[9]};
    So {answers[0]} would, were he not {answers[0]} call’d,
    Retain that dear {answers[10]} which he owes
    Without that title. {answers[0]}, {answers[11]} thy name,
    And for that name, which is no part of thee,
    Take all myself."""

elif choice == 2:
    #                0        1         2           3          4       5         6           7
    bee_libs = "plural noun, noun, plural noun, adjective, adjective, noun, plural noun, adjective".title().split(", ")
    
    for x in bee_libs:
        answers.append(input(x + ": "))

    beemovie = f"""According to all known {answers[0]} of {answers[1]}, there is no way a bee should be able to fly.
    Its {answers[2]} are too {answers[3]} to get its fat {answers[4]} body off the {answers[5]}.
    The Bee, of course, flies anyway, because bees don't care what {answers[6]} think is {answers[7]}."""

elif choice == 3:
    #             0        1        2      3         4        5       6      7     8        9           10          11      12       13
    fit_libs = "sport, adjective, sport, adverb, adjective, number, number, noun, noun, sound word, sound word, adjective, noun, random word".title().split(", ")
    
    for x in fit_libs:
        answers.append(input(x + ": "))

    fitgram = f"""The FitnessGram {answers[0].title()} Test is a multistage {answers[1]} {answers[2]} test that {answers[3]} gets more {answers[4]} as it continues.
    The {answers[5]} meter {answers[0].lower()} test will begin in {answers[6]} seconds. Line up at the {answers[7]}.
    The running {answers[8]} starts slowly but gets faster each minute after you hear this signal {answers[9]}.
    A sing lap should be completed every time you hear this sound. {answers[10]}
    Remember to run in a {answers[11]} {answers[12]} and run as long as possible.
    The second time you fail to complete a lap before the sound, your test is over.
    The test will begin on the word {answers[13]}. On your mark. Get ready!… Start. {answers[10]}"""

print("\n")
if choice == 1:
    print(juliet)
elif choice == 2:
    print(beemovie)
elif choice == 3:
    print(fitgram)
else:
    print("Number not recognised")
