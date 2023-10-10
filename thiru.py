from celery import Celery
import time 
celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Replace with your Redis connection details
    backend="redis://localhost:6379/0",  # Replace with your Redis connection details
)

@celery.task
def add(x, y):
   
    
    return x * y


    
