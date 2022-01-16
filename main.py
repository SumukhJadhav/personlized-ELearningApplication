import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from sklearn import *
from sklearn import linear_model
from sklearn import preprocessing
import json 
""" easy = {"How much is 65-43?": 22,
        "The square root of 144?": 12,
        "How much is 222+83?": 305,
        "Total degrees in the right angle?": 90,
        "What number should be added to 66 to get 121 as a sum?": 55,
        "what is the cube of 5": 125,
        "3/5th of 100 is?": 60,
        "The remainder of 21 divided 7 is?": 0,
        "What is the cube of 7?": 343} """
json_file = open("easy.json")
data = json.load(json_file)

questions = []
answers = []


for i in range(len(data)):
    questions.append(data[i]["question"])
for i in range(len(data)):
    answers.append(data[i]["answer"])

easy = dict(zip(questions, answers))


medium = {"Solve: (2x + 5)/(x + 4) = 1 Give the value of x": -1,
            "Solve: 6x - 19 = 3x - 10 Give the value of x": 3,
            "A fruit seller had some apples. He sells 40% apples and still has 420 apples. How many apples did he originally have?": 700,
            "What percentage of numbers from 1 to 70 have 1 or 9 in the unit's digit?": 20,
            "In a bag full of small balls, 1/4 of these balls are green, 1/8 are blue, 1/12 are yellow and the remaining 26 white. How many balls are blue?": 6, "In a school 50% of the students are younger than 10, 1/20 are 10 years old and 1/10 are older than 10 but younger than 12, the remaining 70 students are 12 years or older. How many students are 10 years old?": 10,
            "The division of a whole number N by 13 gives a quotient of 15 and a remainder of 2. Find N.": 197, "A car is traveling 75 kilometers per hour. How many meters does the car travel in one minute?": 2000, "Tom travels 60 miles per hour going to a neighboring city and 50 miles per hour coming back using the same road. He drove a total of 5 hours away and back. What is the distance from Tom's house to the city he visited?(round your answer to the nearest mile.": 136, "Tom travels 60 miles per hour going to a neighboring city and 50 miles per hour coming back using the same road. He drove a total of 5 hours away and back. What is the distance from Tom's house to the city he visited?(round your answer to the nearest mile.": 136}

hard = {"1. A rectangle field has an area of 300 square meters and a perimeter of 80 meters. What is the width of the field?": 10, "A rectangular garden in Mrs Dorothy's house has a length of 100 meters and a width of 50 meters. A square swimming pool is to be constructed inside the garden. Find the length of one side of the swimming pool if the remaining area(not occupied by the pool) is equal to one half the area of the rectangular garden.": 50, "The numbers x, y, z and w have an average equal to 25. The average of x, y and z is equal to 27. Find w.": 19, "1. Find x so that the numbers 41, 46, x, y, z have a mean of 50 and a mode of 45.": 45, "A is a constant. Find A such that the equation 2x + 1 = 2A + 3(x + A) has a solution at x = 2": -0.2,
        "1. 1 liter is equal to 1 cubic decimeter and 1 liter of water weighs 1 kilogram. What is the weight of water contained in a cylindrical container with radius equal to 50 centimeters and height equal to 1 meter?": 250, "A real estate agent received a 6% commission on the selling price of a house. If his commission was $8,880, what was the selling price of the house?": 148000, "An electric motor makes 3,000 revolutions per minutes. How many degrees does it rotate in one second?": 18000, "If a tire rotates at 400 revolutions per minute when the car is traveling 72km/h, what is the circumference of the tire?": 3, "In a shop, the cost of 4 shirts, 4 pairs of trousers and 2 hats is $560. The cost of 9 shirts, 9 pairs of trousers and 6 hats is $1,290. What is the total cost of 1 shirt, 1 pair of trousers and 1 hat?": 150}

df = pd.read_csv(
    r"PROJECT_DATASET.csv")

nms = list(df.columns.values)
nms.remove("level_change")

# independent variable
x = df[nms]

# dependent variable
y = df.loc[:, 'level_change']

# split train - test df
x_train, x_test, y_train, y_test = model_selection.train_test_split(
    x, y, train_size=0.5, random_state=1)

# train model
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

level = 0
i = 1
number_of_questions = 0


def test(list_of_answers):
    # Creating dataframe of answers for testing
    df = [list_of_answers]
    return pd.DataFrame(df, columns=['question_one', 'question_two', 'question_three'])


while i <= 3:
    if level == 0:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(easy.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(easy[q]) == ques):
                ans.append(0)
                print('p')
            else:
                ans.append(1)
                print('pp')
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to medium level!!!")
            print()

    elif level == 1:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(medium.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(medium[q]) == ques):
                
                ans.append(0)
            else:
                print('pp')
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to hard level!!!")
            print()
        elif pred > 0:
            level -= 1
            print()
            print("You have been downgraded to the easy level")
            print()

    elif level == 2:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(hard.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(hard[q]) == ques):
                ans.append(0)
            else:
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred > 0:
            level -= 1
            print()
            print("You have been downgraded to the easy level")
            print()

    i += 1
