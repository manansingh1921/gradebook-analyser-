
def print_welcome_message():
    print("="*40)
    print("   Welcome to the GradeBook Analyzer")
    print("="*40)
    print("You will be prompted to enter student names and marks.")
    print("Type 'done' for the student name when you are finished.")
    print("-" * 40)

def custom_len(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count

def custom_sum(values_list):
    total = 0
    for value in values_list:
        total += value
    return total

def simple_sort(number_list):
    sorted_list = list(number_list) 
    n = custom_len(sorted_list)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
                swapped = True
        
        if not swapped:
            break
    return sorted_list

def get_student_data():
    marks_dict = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            if custom_len(marks_dict) == 0:
                print("No data entered. Please enter at least one student.")
                continue
            else:
                break
        
        mark_str = input(f"Enter mark for {name}: ").strip()
        
        try:
            mark = int(mark_str)
            if 0 <= mark <= 100:
                marks_dict[name] = mark
                print(f"Added {name} with mark {mark}.")
            else:
                print("Invalid mark. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Mark must be a number.")
            
    print("-" * 40)
    print("Data entry complete.")
    return marks_dict

def find_max_score(marks_dict):
    values = marks_dict.values()
    
    first_value = next(iter(values))
    max_val = first_value

    for score in values:
        if score > max_val:
            max_val = score
    return max_val

def find_min_score(marks_dict):
    values = marks_dict.values()
    
    first_value = next(iter(values))
    min_val = first_value

    for score in values:
        if score < min_val:
            min_val = score
    return min_val

def find_students_with_score(marks_dict, target_score):
    students = []
    for name, score in marks_dict.items():
        if score == target_score:
            students.append(name)
    return students

def calculate_average(marks_dict):
    values = list(marks_dict.values())
    total = custom_sum(values)
    count = custom_len(values)
    
    if count == 0:
        return 0.0
    
    return total / count

def calculate_median(marks_dict):
    values = list(marks_dict.values())
    sorted_values = sorted(values)
    count = custom_len(sorted_values)

    if count == 0:
        return 0.0

    mid_index = count // 2

    if count % 2 == 1:
        median = sorted_values[mid_index]
    else:
        val1 = sorted_values[mid_index - 1]
        val2 = sorted_values[mid_index]
        median = (val1 + val2) / 2
        
    return median

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def get_grade_distribution(grades_dict):
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution

def get_pass_fail_lists(marks_dict):
    passed_students = []
    failed_students = []
    for name, score in marks_dict.items():
        if score >= 40:
            passed_students.append(name)
        else:
            failed_students.append(name)
    
    return (passed_students, failed_students)

def print_results_table(marks_dict, grades_dict):
    print("\n--- Full Grade Report ---")
    print("Name\t\tMark\t\tGrade")
    print("----\t\t----\t\t----")
    
    for name, mark in marks_dict.items():
        grade = grades_dict.get(name, 'N/A')
        print(f"{name}\t\t{mark}\t\t{grade}")

def main():
    print_welcome_message()
    
    while True:
        marks = get_student_data()
        
        print("\n" + "="*40)
        print("         Analysis Report")
        print("="*40)

        print("\n--- Statistical Analysis ---")
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)
        
        top_students = find_students_with_score(marks, max_score)
        bottom_students = find_students_with_score(marks, min_score)
        
        print(f"Average Mark: {avg:.2f}")
        print(f"Median Mark:  {median:.1f}")
        print(f"Highest Mark: {max_score} (Scored by: {', '.join(top_students)})")
        print(f"Lowest Mark:  {min_score} (Scored by: {', '.join(bottom_students)})")
        
        print("\n--- Student Grades ---")
        grades = assign_grades(marks)
        
        for name, grade in grades.items():
            print(f"{name}: {grade}")
            
        print("\n--- Pass/Fail Summary (Pass >= 40) ---")
        passed, failed = get_pass_fail_lists(marks)
        
        pass_count = custom_len(passed)
        fail_count = custom_len(failed)
        
        print(f"Total Passed: {pass_count}")
        print(f"Total Failed: {fail_count}")
        
        print("\n--- Grade Counts ---")
        distribution = get_grade_distribution(grades)
        
        for grade, count in distribution.items():
            print(f"Total Grade {grade}: {count} student(s)")
            
        print_results_table(marks, grades)
        
        print("\n" + "="*40)
        
        choice = input("Analyze another set of grades? (yes/no): ").strip().lower()
        if choice != 'yes' and choice != 'y':
            print("Thank you for using the GradeBook Analyzer. Goodbye!")
            break
        
        print("\n" * 2)
        print_welcome_message()

main()
