"""University structure library."""


class Student:
    """A student class."""

    next_id = 1

    def __init__(self, name):
        """Class constructor."""
        self.name = name
        self.id = Student.next_id
        Student.next_id += 1
        self.list_of_subjects = []

    def get_name(self):
        """Get student's name."""
        return self.name

    def get_id(self):
        """Return student ID number."""
        return self.id

    def get_subjects(self):
        """Return subject list."""
        return self.list_of_subjects

    def add_subject(self, subject):
        """Add a subject to the student's list."""
        if subject not in self.list_of_subjects:
            print("Subject is added successfully!")
            self.list_of_subjects.append(subject)
        else:
            print("Such subject already exists.")

    def remove_subject(self, subject):
        """Remove a subject from student's list."""
        if subject in self.list_of_subjects:
            print("Subject is successfully removed!")
            self.list_of_subjects.remove(subject)
        else:
            print("There is no subject to remove!")


class Professor:
    """A professor class."""

    def __init__(self, name):
        """Class constructor."""
        self.name = name
        self.subjects_num = 0

    def get_number_of_subjects(self):
        """Get number of subjects."""
        return self.subjects_num

    def increase_number_of_subjects(self):
        """Increase the subject's num."""
        return self.subjects_num + 1

    def get_name(self):
        """Return professor name."""
        return self.name


class Subjects:
    """A class of subjects."""

    list_of_subjects = []

    def __init__(self, name):
        """Class constructor."""
        self.name = name
        Subjects.list_of_subjects.append(self.name)
        self.subjects = Subjects.list_of_subjects
        self.professor = {}

    def get_name(self):
        """Return subject name."""
        return self.name

    def get_professor(self):
        """Return teaching professor's name."""
        if KeyError:
            print("There is no professor for such subject!")
            return None
        elif ValueError:
            print("There is no subject for this professor!")
            return None
        return self.professor[self.name]

    def set_professor(self, professor):
        """Link between professor and subject."""
        if self.name in self.subjects:
            self.professor[self.name] = professor

    def all_subjects(self):
        """Return all subjects."""
        return self.subjects
