from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Trainer
from .helpers import generate_csv

@receiver(post_save, sender=Trainer)
def generate_csv_on_trainer_save(sender, instance, created, **kwargs):
    if created:  # Only generate CSV when a new Trainer object is created
        generate_csv()
