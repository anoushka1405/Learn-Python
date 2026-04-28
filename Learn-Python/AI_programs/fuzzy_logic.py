'''
To implement fuzzy logic to assign grades based on marks using linguistic categories 
like “Poor”,“Average”,“Good” and “Excellent”.

Fuzzy Logic is a form of many-valued logic derived from fuzzy set theory, where truth values range between 0 and 1 instead of being strictly true or false. It is particularly useful for handling uncertainty and imprecision.
In grading systems, instead of assigning rigid boundaries (like 0–40 = Fail, 40–60 = Pass), fuzzy logic allows smooth transitions between categories such as “Poor,” “Average,” “Good,” and “Excellent.”
Each category is represented using a membership function, which defines the degree to which a given mark belongs to a category.
Example:
A student scoring 55 marks may belong partially to both “Average” and “Good.”
Membership values lie between 0 and 1.

Fuzzy sets used:
Poor (0–40)
Average (30–60)
Good (50–80)
Excellent (70–100)

The final grade is determined based on the highest membership value.

ALGORITHM:
1. Define input variable: marks (0–100).
2. Define fuzzy sets for grades: Poor, Average, Good, Excellent.
3. Create membership functions for each category.
4. Input student marks.
5. Calculate membership values for each fuzzy set.
6. Compare membership values.
7. Assign the grade corresponding to the highest membership.
8. Display the result.

'''
def poor(x):
    if x <= 40:
        return 1
    elif 40 < x <= 50:
        return (50 - x) / 10
    else:
        return 0

def average(x):
    if 30 <= x <= 45:
        return (x - 30) / 15
    elif 45 < x <= 60:
        return (60 - x) / 15
    else:
        return 0

def good(x):
    if 50 <= x <= 65:
        return (x - 50) / 15
    elif 65 < x <= 80:
        return (80 - x) / 15
    else:
        return 0

def excellent(x):
    if 70 <= x <= 100:
        return (x - 70) / 30
    else:
        return 0
    
marks = float(input("Enter marks (0-100): "))
membership_values = {
    "Poor": poor(marks),
    "Average": average(marks),
    "Good": good(marks),
    "Excellent": excellent(marks)
}
grade = max(membership_values, key=membership_values.get)
print(f"Marks: {marks}, Grade: {grade}, Membership Values: {membership_values}")