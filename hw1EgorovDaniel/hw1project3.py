# Plan
# receive inputs from the user
# input 1: how many questions were answered correctly
# input 2: how many questions were on the exam
# print the percentage of questions answered correctly

# gather inputs
correct = eval(input("How many questions were answered correctly? "))
total = eval(input("How many questions were there in total? "))

# do the math
percentage = (correct / total) * 100

# print the result
print(percentage, "percent of the questions were answered correctly")