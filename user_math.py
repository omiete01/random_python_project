import random

# this program will give the user random maths question and score them

def main():
    user_name = input("Please enter your name: ")

    print(f"\nHello, {user_name}! Welcome to the Math Quiz.")
    attempts = 5
    count = 0
    
    for i in range(attempts):
        expr, ans = math_question()
        
        while True:
            print(f"\nWhat is {expr}?")
            user_ans = input("Ans: ")
            
            if user_ans == str(ans):
                count +=1
                print("Correct Answer.")
                break
            else:
                print(f"Thats not right. The correct answer is {ans}")
                break
                
    print(f"Thanks for attempting the quiz. Your score is {count} out of {attempts}")
        

def math_question():
    left = random.randint(1,9)
    right = random.randint(1,9)
    operand = ["+", "*", "-"] #"/"
    
    operator = random.choice(operand)
        
    expr = str(left) + operator + str(right)
    ans = eval(expr)
    
    return expr, ans

main()
