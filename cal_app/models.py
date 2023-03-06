# django imports
from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
	""" to store all the food items that the user wants  """
	name = models.CharField(max_length=200 ,null=False)
	calorie_per_one_quantity = models.FloatField(null=False,default=0)

	def __str__(self):
		return self.name


class Profile(models.Model):
	""" stores all the required data of an user for tracking calories """
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	food_selected = models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.FloatField(default=0)
	total_calorie = models.FloatField(default=0,null=True)
	date = models.DateField(auto_now_add = True)
	calorie_goal = models.PositiveIntegerField(default=0)

	
	def save(self, *args, **kwargs):
		if self.food_selected != None:
			self.amount = (self.food_selected.calorie_per_one_quantity) 
			FoodConsumptionPerDay.calorie_count = self.amount*self.quantity
			self.total_calorie = FoodConsumptionPerDay.calorie_count + self.total_calorie  
			calories = Profile.objects.filter(person_of=self.person_of).last()
			FoodConsumptionPerDay.objects.create(profile=calories,food_name=self.food_selected,calorie_count=FoodConsumptionPerDay.calorie_count,quantity=self.quantity)
			self.food_selected = None
			super(Profile, self).save(*args,**kwargs)
	
		else:
			super(Profile,self).save(*args,**kwargs)



	def __str__(self):
		return str(self.person_of.username)


class FoodConsumptionPerDay(models.Model):
	""" used to store all food consumed by the user """
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
	food_name = models.ForeignKey(Food,on_delete=models.CASCADE)
	calorie_count = models.FloatField(default=0,null=True,blank=True)
	quantity = models.FloatField(default=0)
    
