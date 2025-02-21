from catalogs.base_models import BaseModel


class Tag(BaseModel):

    def __str__(self):
        return self.name
