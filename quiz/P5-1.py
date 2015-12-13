import random

def sampleQuizzes():
    # Your code here
    numTrials = 10000
    bGrade = []
    for i in range(numTrials):
        midterm1 = random.randint(50,80) 
        midterm2 = random.randint(60,90)
        final = random.randint(55,95)
        grade = 0.25*(midterm1 +midterm2) + 0.5*final
        if (grade <75 and grade > 70):
            bGrade.append(grade)
    prob_bGrade = float(len(bGrade))/numTrials
    return prob_bGrade

def plotQuizzes():
    # Your code here
    numTrials = 10000
    scores = generateScores(numTrials)
    pylab.hist(scores, bins = 7, range = (55,90))
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.title('Distribution of Scores')
    pylab.show()
        
