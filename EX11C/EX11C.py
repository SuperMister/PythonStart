"""EX11C."""


import university


def main():
    """Staff with students and professors."""
    liivi = university.Professor("Liivi Kluge")
    neeme = university.Professor("Neeme Loorits")
    matemaatika = university.Subjects("Matemaatika")
    matemaatika.set_professor(liivi)
    progemine = university.Subjects("Programmeerimise algkursus")
    loogiline_progemine = university.Subjects("Loogeline programmeerimine")
    progemine.set_professor(neeme)
    loogiline_progemine.set_professor(neeme)
    martin = university.Student("Martin")
    juri = university.Student("Juri")
    martin.add_subject(matemaatika)
    juri.add_subject(progemine)
    martin.add_subject(loogiline_progemine)
    print(martin.get_subjects_names())
    print(juri.get_subjects_names())
    print(juri.get_name())



main()
