import random


def GenerateRandomInteger(min, max):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Parameters:
    min_value (int): Minimum possible integer value.
    max_value (int): Maximum possible integer value.
    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(min, max)


def ChooseOperator():
    """
    Randomly select a mathematical operator: +, -, or *.
    
    Returns:
    str: A random operator.
    """
    return random.choice(['+', '-', '*'])


def ProblemAndSolution(num1, num2, operator):
    """
    Formulate a math problem based on two numbers and an operator,
    then calculate the correct answer based on the operator.
    
    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The operator, one of +, -, or *.

    Returns:
    The problem (str), and the answer (int).
    """
    # Formulate the problem as a string, e.g., "4 + 5"
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else: 
        # operator == '*'
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Conduct a math quiz with random arithmetic questions. The user is presented with
    questions and must provide the correct answers. The score is displayed at the end.
    """
    score = 0   #Initialize the score to 0
    total_questions = 3 # Set the total number of questions

    print("\nWelcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = GenerateRandomInteger(1, 10)
        num2 = GenerateRandomInteger(1, 5)
        operator = ChooseOperator()

        # Create the math problem and calculate the correct answer
        problem, answer = ProblemAndSolution(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for non integer values
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
            
            if useranswer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input!! Enter a correct intreger answer")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
