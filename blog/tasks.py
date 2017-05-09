from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import Post, Comment
from .utility.crawler import Crawler
from django.contrib.auth.models import User


logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="add",
    ignore_result=True
)
def add():
    logger.info("fuuck u: ")
    crawler = Crawler('程式')
    result = crawler.start()

    post = Post()
    post.author = User.objects.get(username='jjj')
    post.title = result['title']
    post.text = result['text']
    post.publish()
    post.save()
