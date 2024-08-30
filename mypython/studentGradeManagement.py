import json
# student_grades.py

# Define the student data with names and their scores in different subjects
students_scores = {
    "Alice": [88, 92, 85, 90],
    "Bob": [78, 81, 77, 79],
    "Charlie": [90, 85, 88, 92],
    "David": [65, 70, 68, 60]}


# Define the passing threshold
passing_threshold = 75

# Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to determine pass/fail status
def determine_pass_fail(average_score, threshold):
    return "Pass" if average_score >= threshold else "Fail"

# Process each student and store results in a dictionary
results = {}

for student, scores in students_scores.items():
    average_score = calculate_average(scores)
    pass_fail_status = determine_pass_fail(average_score, passing_threshold)
    results[student] = {
        "Scores": scores,
        "Average Score": average_score,
        "Status": pass_fail_status
    }

# Print results
for student, result in results.items():
    print(f"Student: {student}")
    print(f"Scores: {result['Scores']}")
    print(f"Average Score: {result['Average Score']:.2f}")
    print(f"Status: {result['Status']}")
    print("-" * 30)



