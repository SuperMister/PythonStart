"""EX11C."""


import university


def main():
    """Good staff with students and professors."""
    liivi = university.Professor("Liivi Kluge")
    neeme = university.Professor("Neeme Loorits")
    matemaatika = university.Subjects("Matemaatika")
    matemaatika.set_professor(liivi)
    progemine = university.Subjects("Programmeerimise algkursus")
    loogiline_progemine = university.Subjects("Loogiline programmeerimine")
    progemine.set_professor(neeme)
    loogiline_progemine.set_professor(neeme)
    black_widow = university.Student("Nicki Minaj")
    justin = university.Student("Justin Bieber")
    black_widow.add_subject(matemaatika)
    justin.add_subject(progemine)
    black_widow.add_subject(loogiline_progemine)
    print(black_widow.get_subjects_names())
    print(justin.get_subjects_names())
    print(justin.get_name())

main()
