from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=100)
    steps_cooking = models.CharField(max_length=100)
    time_cooking = models.CharField(max_length=30)
    image_dish = models.ImageField(upload_to='recipes/')
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Рецепт: {self.title}."


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    recipe = models.ManyToManyField(Recipe)
