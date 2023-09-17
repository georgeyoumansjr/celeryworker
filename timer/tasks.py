# tasks.py (inside your Django app)

from .celery import shared_task

@shared_task
def my_background_task():
    # Your task code here
    print("Hello, World")



