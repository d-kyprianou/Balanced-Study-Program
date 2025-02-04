import random

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Whoops, please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Whoops, please enter a valid integer.")

def get_study_guide_structure():
    sections = {}
    total_problems = 0
    
    num_sections = get_valid_integer("How many sections in the study guide? ")
    
    for i in range(1, num_sections + 1):
        num_subsections = get_valid_integer(f"How many problems are in Section {i}? ")
        sections[i] = num_subsections
        total_problems += num_subsections

    return sections, total_problems

def pick_random_problem(sections, total_problems):
    weighted_choices = []
    
    for section, subsections in sections.items():
        weighted_choices.extend([(section, i + 1) for i in range(subsections)])

    return random.choice(weighted_choices)

def main():
    print("Welcome to the weighted study guide. We'll need some information to properly randomize and give you a balanced study.")
    print("-----")
    
    sections, total_problems = get_study_guide_structure()
    problem_count = 0
    
    while True:
        prompt = input(f"\nReady for problem {problem_count + 1}? (y/n): ").strip().lower()
        if prompt == "n":
            print(f"Good luck on the exam! You attempted {problem_count} problems.")
            break
        elif prompt == "y":
            section, subsection = pick_random_problem(sections, total_problems)
            problem_count += 1
            print(f"\n         Try Section {section}, problem {subsection}.")
        else:
            print("That won't work! Try 'y' or 'n'.")

if __name__ == "__main__":
    main()
