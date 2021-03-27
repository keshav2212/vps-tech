from django.db import models
class Member(models.Model):
	Name=models.CharField(max_length=50)
	MobileNo=models.IntegerField()
	Email=models.CharField(max_length=50,unique=True)
	Password=models.CharField(max_length=200)
	Department=models.CharField(max_length=50)
	Profilepic=models.ImageField(upload_to='profile')
	Age=models.IntegerField()
	Address=models.CharField(max_length=200)
	add_member=models.BooleanField(default=False)
	delete_member=models.BooleanField(default=False)
	all_member=models.BooleanField(default=False)
	edit_user=models.BooleanField(default=False)
	statics=models.BooleanField(default=False)
	def __str__(self):
		return self.Name
# Create your models here.
