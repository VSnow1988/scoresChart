import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0


def scoresChart():
    scores = []
    for x in range (0,10):
        scores.append(random.randint(0, 100))
    for i in scores:
        if (i >= 90):
            print "Score:" + str(i) + "; Your Grade is A."
        elif (i >= 80):
            print "Score:" + str(i) + "; Your Grade is B."
        elif (i >= 70):
            print "Score:" + str(i) + "; Your Grade is C."
        elif (i >= 60):
            print "Score:" + str(i) + "; Your Grade is D."
        else:
            print "Score:" + str(i) + "; Your Grade is F."



scoresChart()
