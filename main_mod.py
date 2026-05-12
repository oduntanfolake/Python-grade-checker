import input_mod
import logic_mod
import output_mod

def run_program():
    try:
        # 1. Get Input
        score = input_mod.get_score()
        
        # 2. Process Logic
        grade = logic_mod.determine_grade(score)
        
        # 3. Show Output
        output_mod.show_grade(score, grade)
    except ValueError:
        print("Error: Please enter a valid numerical score.")

if __name__ == "__main__":
    run_program()
