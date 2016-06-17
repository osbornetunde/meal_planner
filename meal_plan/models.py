from django.db import models

class Meal(models.Model):
    """Meal for to be eaten"""
    text = models.CharField(max_length=200)
    date_eaten = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
        
        
class Nutrient(models.Model):
    """The class of nutrient of the food"""
    meal = models.ForeignKey(Meal)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Nutrients'
        
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
