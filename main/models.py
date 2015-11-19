from django.db import models

from django.contrib.auth.models import User
import datetime

# Primenit migraziu    python manage.py migrate --fake-initial
# Primenit migraziu    python manage.py migrate --fake main


class QuestionManager(models.Manager):
	def newest(self):
		return self.order_by('-id') # po otdelnomu poly
	def hot(self):
		return self.order_by('-rating')

class Profile(models.Model):
	user = models.OneToOneField(User)
	rating = models.IntegerField()
	avatar = models.ImageField()


class Tag(models.Model):
	name = models.CharField(max_length = 2)
	def __unicode__(self):
		return self.name

class Question(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	rating = models.IntegerField(default = 0)
	created = models.DateTimeField(default  = datetime.datetime.now)
	tags = models.ManyToManyField(Tag)
	likes = models.ForeignKey(User)
	objects = QuestionManager()
	def __unicode__(self):
		return self.title

	

class Answer(models.Model):
	user = models.ForeignKey(Profile)
	question = models.ForeignKey(Question)
	text = models.TextField()
	created = models.DateTimeField(default = datetime.datetime.now)
	#objects = QuestionManager()
	def __unicode__(self):
		return self.text



# Create your models here.
# python manage.py makemigration
