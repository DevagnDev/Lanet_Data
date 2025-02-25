from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name} {self.first_name} teaches {self.subject}."
        # return {"name": self.first_name, "subject": self.subject}


