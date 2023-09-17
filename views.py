from django.shortcuts import render

from .tasks import my_background_task

def some_view(request):
    # Call the Celery task asynchronously
    result = my_background_task.delay()
    return HttpResponse("Task started with ID: {}".format(result.id))

