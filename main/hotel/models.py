from django.db import models
    
class Guest(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    phone = models.CharField(max_length=15)
    nights = models.IntegerField(default= 1)
    bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_taken = models.BooleanField(default= False)
    
    def __str__(self):
        return f"{self.name}.{self.room_number}"
    