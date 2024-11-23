from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f'{self.name} {self.email}'

    def __str__(self):
        return f"Author: {self.name} email: {self.email}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.CharField(max_length=100)
    steps_cooking = models.TextField()
    time_cooking = models.TextField()
    image_dish = models.ImageField(upload_to='recipes/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    recipe = models.ManyToManyField(Recipe)
