def get_student_score():
    try:
        return float(input("Enter the student's score (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def calculate_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def display_result(score, grade):
    print(f"\n--- Results ---")
    print(f"Score: {score}")
    print(f"Grade: {grade}")

def main():
    score = get_student_score()
    if score is not None:
        grade = calculate_grade(score)
        display_result(score, grade)

if __name__ == "__main__":
    main()
