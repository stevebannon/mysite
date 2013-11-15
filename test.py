from polls.models import Poll,Choice
from django.utils import timezone
Poll.objects.all()
p = Poll(question = "What's new?",pub_date=timezone.now())
p.save()
p.id
p.question
p.pub_date
Poll.objects.filter(id=1)
Poll.objects.filter(question__startswith='What')

