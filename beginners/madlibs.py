print("""
Mad Libs Generator!
1: Romeo and Juiet
2: Bee Movie
3: FitGram Pacer Test

""")

choice = int(input("Enter a number: "))
answers = []

###############################################################################
#               0    1    2    3    4    5    6    7    8       9      10   11
juliet_libs = "name noun noun noun noun noun noun noun verb adjective noun verb".title().split()

if choice == 1:
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
###############################################################################

###############################################################################
#                0        1     2         3           4          5       6         7           8
bee_libs = "plural noun, noun, noun, plural noun, adjective, adjective, noun, plural noun, adjective".title().split(", ")

if choice == 2:
  for x in bee_libs:
    answers.append(input(x + ": "))

beemovie = f"""According to all known {answers[0]} of {answers[1]}, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The Bee, of course, flies anyway, because bees don't care what humans think is impossible."""
###############################################################################

###############################################################################
#
fit_libs = "".title().split()

if choice == 2:
  for x in fit_libs:
    answers.append(input(x + ": "))

fitgram = f"""The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.
The 20 meter pacer test will begin in 30 seconds. Line up at the start.
The running speed starts slowly but gets faster each minute after you hear this signal bodeboop.
A sing lap should be completed every time you hear this sound. ding
Remember to run in a straight line and run as long as possible.
The second time you fail to complete a lap before the sound, your test is over.
The test will begin on the word start. On your mark. Get ready!… Start. ding"""
###############################################################################

###############################################################################
print("\n")
if choice == 1:
    print(juliet)
elif choice == 2:
    print(beemovie)
elif choice == 3:
    print(fitgram)
