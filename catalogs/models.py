from .base_models import BaseModel


class Category(BaseModel):

    def __str__(self):
        return self.name