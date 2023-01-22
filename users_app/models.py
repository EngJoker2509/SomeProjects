from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(null=True)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
    description=models.TextField(null=True)

    def __str__(self):
        return f"<Movie object: ({self.first_name}) ({self.last_name}) ({self.email_address}) ({self.age}) \n >"

# last_user=users.objects.last()
# print(last_user.__str__())
# first_user=users.objects.first()
# print(first_user.__str__())


# user_with_3 = users.objects.get(id=30)
# user_with_3.first_name = 'Pancakes'
# user_with_3.save()

    def delete(id): 
        user_with_2=users.objects.get(id=id)
        return user_with_2.delete()

    def create(first_name,last_name,email_address,age):
        return users.objects.create(first_name=first_name,last_name=last_name,email_address=email_address,age=age)

        
# user=users.objects.all().order_by('first_name')
# userDesc=users.objects.all().order_by('-first_name')


# for user in userDesc:
#     print(user.__str__())