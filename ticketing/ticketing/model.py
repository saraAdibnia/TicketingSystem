from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)

class User(models.Model):
    role= models.IntegerField(default=1)
    mobile = models.CharField(max_length=11) #for example 09123456789
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    subject = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)



class File(models.Model):
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=100)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)


class Answer(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)

