import random

print("Welcome to the weighted study guide. We'll need some information to properly randomize and give you a balanced study.")
print("-----")

def get_study_guide_structure():
    sections = {}
    total_problems = 0
    
    num_sections = int(input("How many sections in the study guide? "))
    
    for i in range(1, num_sections + 1):
        num_subsections = int(input(f"How many subsections are in Section {i}? "))
        sections[i] = num_subsections
        total_problems += num_subsections

    return sections, total_problems

def pick_random_problem(sections, total_problems):
    weighted_choices = []
    
    for section, subsections in sections.items():
        weighted_choices.extend([(section, i + 1) for i in range(subsections)])

    return random.choice(weighted_choices)

def main():
    sections, total_problems = get_study_guide_structure()
    
    while True:
        prompt = input("\nReady for a problem? (y/n): ").strip().lower()
        if prompt == "n":
            print("Good luck on the exam, soldier.")
            break
        elif prompt == "y":
            section, subsection = pick_random_problem(sections, total_problems)
            print(f"\nTry {section}, Subsection {subsection}.\n")
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
