from django.contrib.auth.models import User

from django.db import models

def upload_to(instance, filename):
    # Customize the directory structure as per your needs
    return f'Mainapp/static/Images/{filename}'
class Question(models.Model):
    image1 = models.ImageField(blank=True,null=True,upload_to=upload_to)
    image2 = models.ImageField(blank=True,null=True,upload_to=upload_to)
    image3 = models.ImageField(blank=True,null=True,upload_to=upload_to)
    text = models.TextField()
    code = models.TextField()

    def __str__(self):
        return str(self.id)

class QuestionAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    solved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


