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

    def get_subjects_names(self):
        """Get names of subjects that students study."""
        list_subjects = []
        for i in range(len(self.list_of_subjects)):
            list_subjects.append(self.list_of_subjects[i].name)
        return "Subjects that " + self.name + " studies: " + str(list_subjects)

    def get_subjects(self):
        """Return subject list."""
        return self.list_of_subjects

    def add_subject(self, subject):
        """Add a subject to the student's list."""
        if subject.__class__ is Subjects:
            if subject not in self.list_of_subjects:
                print("Subject is successfully added to " + self.name + "'s timetable!")
                self.list_of_subjects.append(subject)
            else:
                print("Subject has not been added. Such subject already exists. ")
        else:
            print("There is no such subject in our university. Try again!")

    def remove_subject(self, subject):
        """Remove a subject from student's list."""
        if subject in self.list_of_subjects:
            print("Subject is successfully removed from" + self.name + "'s timetable!")
            self.list_of_subjects.remove(subject)
        else:
            print("There is no such subject to remove!")


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
        self.subjects_num += 1
        print("The number of subjects for professor " + self.name + " is increased by 1!")

    def get_name(self):
        """Return professor name."""
        return self.name


class Subjects:
    """A class of subjects."""

    all_subjects = []

    def __init__(self, name):
        """Class constructor."""
        self.name = name
        Subjects.all_subjects.append(self)
        self.professor = None

    def get_name(self):
        """Return subject name."""
        return self.name

    def get_professor(self):
        """Return teaching professor's name."""
        return self.professor

    def set_professor(self, professor):
        """Link between professor and subject."""
        if professor.__class__ == Professor:
            self.professor = professor
            professor.increase_number_of_subjects()
            print("Now there is a professor for subject: " + self.name)
        else:
            print("This guy is not a fucking professor!")
