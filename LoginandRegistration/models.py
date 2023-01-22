from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(null=True)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)

    def __str__(self):
        return f"<Movie object: ({self.first_name}) ({self.last_name}) ({self.email_address})) \n >"