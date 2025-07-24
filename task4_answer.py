courses = ["MTH 101", "PHY 101", "CHM 101", "CSC 101", "GST 101"]

courses.insert(0, "ENG101")

print(courses)

courses.remove("GST 101")

print(courses)

courses.insert(4, "BIO 101")

print(courses)

courses_len = len(courses)

print(f"\nThe total number of courses the student is now offering is = ", courses_len)

print(f"\nThe student's third course in the list is: ", courses[2])
