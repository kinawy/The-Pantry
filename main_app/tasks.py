from celery import shared_task
from django.utils import timezone
from .models import Post

@shared_task
def delete_old_posts():
    posts = Post.objects.all()

    for post in posts:
        if post.expiration_date < timezone.now():
            post.delete()

    return "Completed deleting all expired posts"