from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()

    @classmethod
    def get_location(cls):
        place = cls.objects.all()
        return place

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    img_location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['-image']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()