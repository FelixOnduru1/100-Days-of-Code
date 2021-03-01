import random
names = ["Felix", "Maggie", "Mary"]
scores = {name: random.randint(0, 99) for name in names}
print(scores)

passed_students = {name: score for(name, score) in scores.items() if score > 59}
print(passed_students)
