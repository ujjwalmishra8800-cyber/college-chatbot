questions_answers = {
    "fees kya hai": "BCA AIML fees is 95,000 per year.",
    "hostel available hai": "Yes, hostel facility is available for boys and girls.",
    "admission process kya hai": "You can apply online through the college website.",
    "exam kab honge": "Exams will start next month.",
    "library available hai": "Yes, the college library is available for all students.",
    "attendance kitni chahiye": "Minimum 75% attendance is required.",
}

# Auto-generate 500 college-related questions and answers
for i in range(1, 501):
    questions_answers[f"bca question {i}"] = f"This is answer number {i} for BCA students."
    questions_answers[f"hostel query {i}"] = f"Hostel information response {i}."
    questions_answers[f"fees query {i}"] = f"Fees related response {i}."
    questions_answers[f"exam query {i}"] = f"Exam related response {i}."
    questions_answers[f"placement query {i}"] = f"Placement related response {i}."

# Total questions will become more than 2500 automatically
print(f"Total Questions Loaded: {len(questions_answers)}")
