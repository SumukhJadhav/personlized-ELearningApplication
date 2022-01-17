import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from sklearn import *
from sklearn import linear_model
from sklearn import preprocessing
import json 

json_file = open("test.json")
data = json.load(json_file)

level_1 = {d["Questions"] : d["Answers"] for d in data if d["Difficulty"] == 1}
level_2 = {d["Questions"] : d["Answers"] for d in data if d["Difficulty"] == 2}
level_3 = {d["Questions"] : d["Answers"] for d in data if d["Difficulty"] == 3}
level_4 = {d["Questions"] : d["Answers"] for d in data if d["Difficulty"] == 4}
level_5 = {d["Questions"] : d["Answers"] for d in data if d["Difficulty"] == 5}

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


while i <= 5:
    if level == 0:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(level_1.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(level_1[q]) == ques):
                ans.append(0)
            else:
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to 2nd level!!!")
            print()

    elif level == 1:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(level_2.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(level_2[q]) == ques):
                
                ans.append(0)
            else:
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to 3rd level!!!")
            print()
        elif pred > 0:
            level -= 1
            print()
            print("You have been downgraded to the 1st level")
            print()
    
    elif level == 2:

        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(level_3.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(level_3[q]) == ques):
                ans.append(0)
            else:
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to 4th level!!!")
            print()
        elif pred > 0:
            level -= 1
            print()
            print("You have been downgraded to the 2nd level")
            print()

    elif level == 3:

        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(level_4.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(level_4[q]) == ques):
                ans.append(0)
            else:
                ans.append(1)
            a += 1
        x_test = test(ans)
        y_pred = regr.predict(x_test)
        pred = round(y_pred[0])
        if pred == 0:
            level += 1
            print()
            print("You have successfully upgraded to 5th level!!!")
            print()
        elif pred > 0:
            level -= 1
            print()
            print("You have been downgraded to the 3rd level")
            print()

    elif level == 4:
        a = 0
        ans = []  # List of answers whether true or false
        # Getting the list of questions
        questions = list(level_5.keys())
        while a < 3:
            # Selecting a random question and asking
            q = rd.choice(questions)
            questions.remove(q)
            ques = (input(q+" - "))
            number_of_questions += 1  # Incrementing the total number of questions
            if (str(level_5[q]) == ques):
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
            print("You have been downgraded to the idk level")
            print()

    i += 1
