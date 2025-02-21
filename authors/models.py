from django.db import models
from catalogs.base_models import BaseModel


class Author(BaseModel):
    photo = models.ImageField(upload_to='authors_photos/')

    def __str__(self):
        return self.name