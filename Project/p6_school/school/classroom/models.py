from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name} {self.first_name} teaches {self.subject}."
        # return {"name": self.first_name, "subject": self.subject}


    # def teacher_detail(request, id):
    # # Retrieve the teacher or return a 404 error if not found
    # teacher = get_object_or_404(Teacher, id=id)
    # # Build a dictionary with the teacher's information
    # data = {
    #     "first_name": teacher.first_name,
    #     "last_name": teacher.last_name,
    #     "subject": teacher.subject,
    #     # Optionally include the string representation if needed:
    #     "description": str(teacher),
    # }
    # # Return the data as a JSON response
    # return JsonResponse(data)