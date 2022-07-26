from django.db import models

def img_upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

def file_upload_to(instance, filename):
    return 'documents/{filename}'.format(filename=filename)

class Classification(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Object(models.Model):
    name = models.TextField()
    image_url = models.ImageField(upload_to=img_upload_to)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    order = models.TextField()
    family = models.TextField()
    status = models.TextField()
    distribution = models.TextField()
    habitat = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    protection = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.TextField()
    file_url = models.FileField(upload_to=file_upload_to)

    def __str__(self):
        return self.name
        