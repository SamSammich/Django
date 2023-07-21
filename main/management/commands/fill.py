from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **optionns):
        student_list = [
            {'last_name': 'Sahkivech', 'first_name': 'Shama'},
            {'last_name': 'Obramov', 'first_name': 'Roman'},
            {'last_name': 'Rasulov', 'first_name': 'Renat'},
            {'last_name': 'Sammich', 'first_name': 'Sam'},
            {'last_name': 'Seronov', 'first_name': 'Salamon'},
            {'last_name': 'Ibragimov', 'first_name': 'Simon'},
            {'last_name': 'Jack', 'first_name': 'Petr'},
            {'last_name': 'Jacob', 'first_name': 'Jack'},
            {'last_name': 'Jekki', 'first_name': 'Jan'},

        ]
        # for student_item in student_list:
        #   Student.objects.create(**student_item)
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)
