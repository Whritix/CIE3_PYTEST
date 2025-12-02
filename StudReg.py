import pytest
def student_Regestration(student_id,student_name,course_enrolled,academic_year):
    result=(
        f"Student ID: {student_id}\n"
        f"Student Name: {student_name}\n"
        f"Course Enrolled: {course_enrolled}\n"
        f"Academic Year: {academic_year}"
    )
    return result
if __name__ == "__main__":
    student_id="102"
    student_name="ADITYA"
    course_enrolled="BCA"
    academic_year="2025-2026"
    print(student_Regestration(student_id,student_name,course_enrolled,academic_year))