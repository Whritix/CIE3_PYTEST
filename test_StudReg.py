from StudReg import student_Regestration

def test_student_registration():
    expected_output = (
        "Student ID: 102\n"
        "Student Name: ADITYA\n"
        "Course Enrolled: BCA\n"
        "Academic Year: 2025-2026"
    )
    assert student_Regestration("102", "ADITYA", "BCA", "2025-2026") == expected_output