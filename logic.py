#THIS IS MY OWN CODE*

"""This program will test your programming logic

It uses dictionary key:value pairs
a point counter for correct answers
a function to add points
"""
from datetime import datetime
startTime = datetime.now()
truth_tables = {"not False": True, "not True": False, 
                "True or False": True, "True or True": True, "False or True": True, "False or False": False,
                "True and False": False, "True and True": True, "False and True": False, "False and False": False,
                "not True or False": False, "not True or True": False, "not False or True": False, "not False or False": True,
                "not True and False": True, "not True and True": False, "not False and True": True, "not False and False": True,
                "1 != 0": True, "1 != 1": False, "0 != 1": True, "0 != 0": False,
                "1 == 0": False, "1 == 1": True, "0 == 1": False, "0 == 0": True}

# Add points to score
def add_point(points):
    return points + 1

# Ask question
def main():
    #correct_answers = {}
    score = 0
    reward = ""
    print("True or False?")
    for key_value in truth_tables.items():
        print(key_value[0])
        answer = input()
        if answer.lower() == str(key_value[1]).lower():
            score = add_point(score)
        else:
            score
            #correct_answers.update(key_value)


        if score <= 13:
            reward = "You failed! :D"
        elif score > 13 and score < 20:
            reward = "Doing okay!"
        elif score >= 20 and score < 26:
            reward = "Almost there!"
        elif score == 26:
            reward = "Perfect score"

    print(str(score) + "/26" + f": {reward}")
    #if len(correct_answers) != 0:
        #print(correct_answers)



print(len(truth_tables))
main()
print(f"Time to completion: {datetime.now() - startTime}")
