print('Welcome to Favours quiz!')

playing = input('would you like to play? ').lower()

if playing != 'yes':
    quit()

print('okay! Lets play :)')
score = 0

answer = input("what is the full meaning of U.I? ")
if answer.lower() == "university of ibadan":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("The correct answer is university of ibadan.")

answer = input("what does FMU stand for? ")
if answer.lower() == "free minded uites":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("The correct answer is Free Minded Uites ")

answer = input("What department is Favour in? ").lower()
if answer == "sociology":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("The correct answer is Sociology.")

answer = input("where is U.I located? ")
if answer.lower() == "ibadan":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("The correct answer is Ibadan.")

answer = input("Who is the owner of the popular ice cream brand named Bunnyberry? ")
if answer.lower() == "prince":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("The correct answer is Prince")

answer = input("Do You Like My Quiz? ")
if answer.lower() == "yes":
    print("yaaaayyy")
    score += 1
else:
    print(":(")
    print("sigh")

print('you got ' + str(score) + ' questions correct!')



