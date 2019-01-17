from django.db import models

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	location = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	appLink = models.CharField(max_length=10000)

	class Meta:
		verbose_name = "Job"
		verbose_name_plural = "Jobs"

	def __str__(self):
		return self.title


