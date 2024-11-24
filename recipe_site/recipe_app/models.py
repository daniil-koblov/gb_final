from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    steps_cooking = models.CharField(max_length=200)
    time_cooking = models.CharField(max_length=30)
    image_dish = models.ImageField(upload_to='media/recipes/')
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Рецепт: {self.title}."

