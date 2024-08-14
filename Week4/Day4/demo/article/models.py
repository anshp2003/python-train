from django.db import models

# Create your models here.



from django.db import models

class Article2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
    # Order the articles by the created date, newest first
        ordering = ['-created_at']
    
        # Set a human-readable name for the model
        verbose_name = "Article"
        verbose_name_plural = "Articles"


    def __str__(self):
        return self.title
