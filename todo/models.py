from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return self.item[:20]