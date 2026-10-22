# Project Name: Quiz Application

print("Welcome to Quiz Application!")

score = 0


print("\n1. What is the capital of India?")
print("A. Chennai")
print("B. New Delhi")
print("C. Mumbai")
answer = input("Enter your answer: ").upper()


if answer == "B":
    print("Correct Answer!")
    score += 1

else:
    print("Wrong Answer!")

print("\n2. What is 5 + 5?")
print("A. 10")
print("B. 15")
print("C. 20")
answer = input("Enter your answer: ").upper()


if answer == "A":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")


print("\nYour Score:", score, "/ 2")
print("Thank you for playing!")