from django.db import models
from PIL import Image
from django.core.files import File
from io import BytesIO

#image compression method
def compress(image):
    img = Image.open(image)
    img_io=BytesIO()
    img.resize((120,100)).convert("RGB").save(img_io, 'jpeg')
    new_img=File(img_io,name=image.name)
    return new_img

class Person(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', max_length= 120,default=None)

    #calling image compression function before saving the data
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)