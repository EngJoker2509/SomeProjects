from django.db import models


class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True, default='Hello')

    def create(name, city, state):
        dojos.objects.create(name=name, city=city,
                             state=state, desc='I love You')

    def dojos_delete(id):
        print(f'id={id}')
        user_delete = dojos.objects.get(id=id)
        #user_delete_reverse=ninjas.objects.get(dojos_id=id)
        #print(user_delete_reverse)
        user_delete.delete()

    def retive_first():
        _dojos = dojos.objects.first()
        for i in _dojos.dojos_id.all():
            print(i.dojo, i.first_name, i.last_name)

    def retive_last():
        _dojos = dojos.objects.last()
        for i in _dojos.dojos_id.all():
            print(i.dojo, i.first_name, i.last_name)


class ninjas(models.Model):
    dojo = models.ForeignKey(dojos, related_name="dojos_id", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def create(first_name, last_name, id):
        ninjas.objects.create(dojo=dojos.objects.get(id=id),first_name=first_name, last_name=last_name)
    
    def ninja_delete(id):
        dojo_id=dojos.objects.get(id=id)
        users_ninjas = ninjas.objects.filter(dojo=dojo_id)
        users_ninjas.delete()