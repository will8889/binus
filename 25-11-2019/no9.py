def get_grade(score:float):
    return "error" if score > 1.0 else "A" if score >= 0.9 and score <= 1.0 else "B" if score >= 0.8 and score <= 1.0 else "C" if score >= 0.8 and score <= 1.0 else "D" if score >= 0.6 and score <= 1.0 else "F"

print(get_grade(0.8))