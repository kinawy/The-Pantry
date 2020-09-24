from celery import shared_task
from django.utils import timezone
from .models import Post

# function to delete every post that is younger than the time set in the task
# shared task is a helper function from celery
@shared_task
def delete_old_posts():
    posts = Post.objects.all()

    # loop through the Post table and do our task
    for post in posts:
        if post.expiration_date < timezone.now():
            post.delete()

    return "Completed deleting all expired posts"