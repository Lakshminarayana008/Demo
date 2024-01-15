def grade(score):
    if score > 100:
        return "wrong score"
    if score >= 90:
        return "grade A"
    if score >= 80:
        return "grade B"
    if score >= 70:
        return "grade C"
    if score >= 60:
        return "grade D"
    return "Your grade is an F"

score = float(input("Enter Score Grade:"))
print (grade(score))