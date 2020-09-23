classGrades = {"Ann": [20, 45, 15], "Bob": [12, 34, 39], "Clyde": [50, 17, 43], "Denise": [10, 50, 25]}
#You need a 25 average to pass - who in the class has passed?
#Which of the three tests did the student do the best in?
#What is the average score in the class for the final test?
#What is the average score in the class in all the tests?
#Which student achieved the best grades? Who did the worst?

def averagescore(scores, numberOfTests):
    totalScore = sum(scores)
    return totalScore/numberOfTests

def whoPassed():
    passingStudents = []
    for student, scores in classGrades.items():
        if averagescore(scores, len(scores)) >= 25:
            passingStudents.append(student)
    return passingStudents

def bestTest():
    numberOfTests = 3
    numberOfStudents = 4
    testScores = [0] * numberOfTests #this dictionary has a space for every test
    for i in range(numberOfTests):
        for key, value in classGrades.items():
            testScores[i] = testScores[i] + value[i]
    testAverages = []
    for j in testScores:
        testAverages.append(j/numberOfStudents)
    bestTestScore = max(testAverages)
    return("Test " + (str)((testAverages.index(bestTestScore))+1) + " had the best scores.") #Offset by one.

def averageFinalTest():
    score = 0
    numberOfStudents = 4
    for key, value in classGrades.items():
        score = score + value[-1]
    return(score/numberOfStudents)

def averageOverall():
    numberOfStudents = 4
    score = 0
    for student, scores in classGrades.items():
        score = score + averagescore(scores, len(scores))
    return (score/numberOfStudents)

def bestStudent():
    bestStudent = ""
    max = 0
    for student, scores in classGrades.items():
        if averagescore(scores, len(scores)) > max:
            max = averagescore(scores, len(scores))
            bestStudent = student
    return bestStudent

def worstStudent():
    worstStudent = ""
    min = 1000
    for student, scores in classGrades.items():
        if averagescore(scores, len(scores)) < min:
            min = averagescore(scores, len(scores))
            worstStudent = student
    return worstStudent

print(whoPassed())
print(bestTest())
print(averageFinalTest())
print(bestStudent())
print(worstStudent())
print(averageOverall())