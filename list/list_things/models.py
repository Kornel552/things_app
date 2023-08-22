from django.db import models


class Lista(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Lista, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)
  def __str__(self):
    return self.text
