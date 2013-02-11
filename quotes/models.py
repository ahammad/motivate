from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=64)

class Quote(models.Model):
	CATEGORIES = (
		(1, 'Motivational'),
	)

	quotation = models.CharField(max_length=300)
	author = models.ForeignKey(Author)
	category = models.CharField(max_length=2, choices=CATEGORIES)

