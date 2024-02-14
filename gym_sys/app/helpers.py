import csv
from io import StringIO
from django.core.files.base import ContentFile
from .models import Trainer,TrainerCSV

def generate_csv():# create a function
    header_row=[# this is a Header Row
        '#',
        'username',
        'mobile',
        'salary',
        'address',
        'detail'
    ]
    filename='trainer.csv'# file name that execute
    with StringIO() as  csv_buffer:
        csv_writter=csv.writer(csv_buffer)#create csv buffer
        csv_writter.writerow(header_row)# here Header Row Added
        Trainers=Trainer.objects.all()  # collect all Trainer Data
        for train in Trainers:
            csv_writter.writerow(   #   Here data entry from db to csv
                [
                    train.id,
                    train.username,
                    train.mobile,
                    train.salary,
                    train.address,
                    train.detail,
                ]
            )
        csv_file=ContentFile(
            csv_buffer.getvalue().encode('utf-8')
        )
    trainer_csv=TrainerCSV.objects.create()
    trainer_csv.csv.save(filename,csv_file)# save this file as TrainerCSV model






