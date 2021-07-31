from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Manhwa(models.Model):
    choices = (
        ("Ongoing", "Ongoing"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=choices, max_length=255)
    cover_image = models.ImageField(upload_to="images/cover_images")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags")
    verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return "{} {} {}".format(self.title, self.author, self.status)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Manhwa, self).save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify("{} {}".format(self.first_name, self.last_name))
        super(Author, self).save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)
