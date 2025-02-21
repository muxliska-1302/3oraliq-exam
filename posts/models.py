from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
import uuid


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    full_content = models.TextField()
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('catalogs.Category', on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts_images/')
    posted_at = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('tags.Tag')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if Post.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{uuid.uuid4().hex[:6]}"
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'posts:detail',
            kwargs={
                'year': self.posted_at.year,
                'month': self.posted_at.month,
                'day': self.posted_at.day,
                'slug': self.slug,
            }
        )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    posted_on = models.DateField(auto_now_add=True)
