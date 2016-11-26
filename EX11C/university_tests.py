"""Tests for EX12A."""


import university


def test_student_get_subject_name():
    """Test if function is adding subject to the student's timetable."""
    student = university.Student("Juri")
    matemaatika = university.Subjects("Matemaatika")
    student.add_subject(matemaatika)
    assert student.get_subjects_names() == "Subjects that " + student.name + " studies: ['Matemaatika']"


def test_2_students_get_subject_names():
    """Test if function is getting names of subjects that students study."""
    student = university.Student("Juri")
    student2 = university.Student("Suvaline")
    matemaatika = university.Subjects("Matemaatika")
    student.add_subject(matemaatika)
    student2.add_subject(matemaatika)
    assert student.get_subjects_names() == "Subjects that " + student.name + " studies: ['Matemaatika']"
    assert student2.get_subjects_names() == "Subjects that " + student2.name + " studies: ['Matemaatika']"


def test_student_remove_subject():
    """Test if function is removing subject from student's timetable."""
    student = university.Student("Juri")
    matemaatika = university.Subjects("Matemaatika")
    fuusika = university.Subjects("Fuusika")
    student.add_subject(matemaatika)
    student.add_subject(fuusika)
    student.remove_subject(matemaatika)
    assert student.get_subjects_names() == "Subjects that " + student.name + " studies: ['Fuusika']"


def test_get_name_professor():
    """Test if function is getting professor name."""
    a = university.Professor("Opetaja")
    assert a.get_name() == "Opetaja"


def test_increase_number_of_subjects():
    """Test if function is increasing professor's number of subjects."""
    a = university.Professor("Opetaja")
    a.increase_number_of_subjects()
    assert a.get_number_of_subjects() == 1


def test_professor_and_num_subjects():
    """Test if function is increasing professor's number of subjects by 2 and gives gives his name."""
    a = university.Professor("Opetaja")
    a.increase_number_of_subjects()
    a.increase_number_of_subjects()
    assert [a.get_number_of_subjects(), a.get_name()] == [2, "Opetaja"]


def test_subject_get_name():
    """Test if function is getting the name of subject."""
    matemaatika = university.Subjects("Matemaatika")
    assert matemaatika.get_name() == "Matemaatika"


def test_set_get_professor():
    """Test if functions are setting and getting professor."""
    liivi = university.Professor("Liivi")
    matemaatika = university.Subjects("Matemaatika")
    matemaatika.set_professor(liivi)
    assert matemaatika.get_professor().name == "Liivi"


def test_add_professor_not_professor():
    """Test if functions cannot add professor that is not professor."""
    matemaatika = university.Subjects("Matemaatika")
    assert matemaatika.set_professor("burger") is None
