"""EX11C."""


import university


def main():
    """Staff with students and professors."""
    mati = university.Student("Mati")
    kati = university.Student("Kati")
    print(str(mati.get_id()) + "\t" + mati.get_name())
    mati.add_subject("Matan")
    mati.add_subject("Fuusika")
    mati.add_subject("Progemine")
    print(mati.get_subjects())
    print(str(kati.get_id()) + "\t" + kati.get_name())
    kati.add_subject("Progemine")
    kati.add_subject("fizra")
    kati.add_subject("fizra")
    kati.remove_subject("fizhujak")
    kati.add_subject("matemaatika")
    print(kati.get_subjects())
    prof_1 = university.Professor("Neeme Loorits")
    prof_1.increase_number_of_subjects()
    prof_1.increase_number_of_subjects()
    prof_2 = university.Professor("Gay Richmond")
    prof_2.increase_number_of_subjects()
    prof_1.increase_number_of_subjects()
    print(prof_1.get_number_of_subjects())
    print(prof_2.get_number_of_subjects())
    progemine = university.Subjects("Progemine")
    progemine.set_professor(prof_1)
    matemaatika = university.Subjects("Matemaatika")
    matemaatika.set_professor(prof_2)
    print(matemaatika.get_professor())


main()
