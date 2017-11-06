# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import string
import random
from django.db import models

# Create your models here.
class kirrurl(models.Model):
	url = models.CharField(max_length = 220,)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		print("something")
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = code_generator()
		super(kirrurl,self).save(*args, **kwargs)

	def __unicode__(self):
		return str(self.url)

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	new_code=''
	for _ in range(size):
		new_code += random.choice(chars)
	return new_code

def create_shortcode(instance, size=6):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code


