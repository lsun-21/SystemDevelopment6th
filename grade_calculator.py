def calculate_final_grade(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")

    total = 0
    for score in scores:
        if score < 0 or score > 100:
            raise ValueError("Score out of range")
        total += score

    return total / len(scores)


def letter_grade(final_score):
    if final_score >= 90:
        return "A"
    if final_score >= 80:
        return "B"
    if final_score >= 70:
        return "C"
    if final_score >= 60:
        return "D"
    return "F"
