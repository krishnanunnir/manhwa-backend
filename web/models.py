import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
from mdeditor.fields import MDTextField


class Manhwa(models.Model):
    VERIFICATION_STATUS_VERIFIED = "Verified"
    VERIFICATION_STATUS_UNVERIFIED = "Unverified"
    VERIFICATION_STATUS_REJECTED = "Rejected"

    choices = (
        ("Ongoing", "Ongoing"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
    )

    verification_status_choices = (
        (VERIFICATION_STATUS_VERIFIED, "Verified"),
        (VERIFICATION_STATUS_UNVERIFIED, "Unverified"),
        (VERIFICATION_STATUS_REJECTED, "Rejected"),
    )
    types = (("Manhwa", "Manhwa"), ("Manhua", "Manhua"))
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=choices, max_length=255)
    type = models.CharField(choices=types, max_length=255, default="Manhwa")
    cover_image = models.ImageField(upload_to="images/cover_images")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags", null=True, blank=True)
    verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    verification_status = models.CharField(
        choices=verification_status_choices, max_length=255, default="Unverified"
    )
    alternate_names = models.CharField(
        max_length=750,
        blank=True,
        null=True,
        help_text="Add comma separated values for the alternate names for the manhwa",
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return "{} {} {}".format(self.title, self.author, self.status)

    @property
    def image_tag(self):
        return mark_safe('<img src="/media/%s" height="100" />' % (self.cover_image))

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


class ManhwaList(models.Model):
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=500)
    description = models.TextField()
    manhwas = models.ManyToManyField(Manhwa, blank=True)

    def save(self, *args, **kwargs):
        current_time_as_string = str(datetime.datetime.now())
        self.slug = "%s-%s" % (slugify(current_time_as_string), slugify(self.title))
        super(ManhwaList, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return "`{}` created by `{}`".format(self.title, self.identifier)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=500)
    content = MDTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
