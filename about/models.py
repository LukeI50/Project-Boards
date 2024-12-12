from django.db import models


# Create your models here.
class About(models.Model):
    """
    Model representing the about page.

    Attributes:
        title (CharField): The title of the about page, with a maximum length of 200 characters.
        content (TextField): The content of the about page.
        updated_on (DateTimeField): The date and time when the about page was last updated. This field is automatically
                                   set to the current date and time whenever the model's save method is called.
    """
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
