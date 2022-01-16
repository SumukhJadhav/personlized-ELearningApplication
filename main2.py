import json

json_file = open("easy.json")
data = json.load(json_file)

questions = []
answers = []


for i in range(len(data)):
    questions.append(data[i]["question"])
for i in range(len(data)):
    answers.append(data[i]["answer"])

easy = dict(zip(questions, answers))

result = {d["question"] : d["answer"] for d in data if d["difficulty"] == 3}
print(result)
""" 
for i in range
print(data[1]['question'])
 """
