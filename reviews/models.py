from django.db import models
from django.conf import settings


class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	rating = models.PositiveSmallIntegerField(default=5)
	comment = models.TextField(blank=True)
	image = models.ImageField(upload_to='reviews/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Review({self.user}, {self.rating})"
