import factory
from web.models import Manhwa, Author, Tags


class AuthorFactory(factory.Factory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class TagsFactory(factory.Factory):
    class Meta:
        model = Tags

    name = factory.Faker("word")


class ManhwaFactory(factory.Factory):
    class Meta:
        model = Manhwa

    title = factory.Faker("sentence", nb_words=4)
    author = factory.SubFactory(AuthorFactory)
    tags = factory.LazyAttribute(lambda a: Tags.objects.all())
    status = 1
    description = factory.Faker("sentence", nb_words=20)
    cover_image = factory.django.ImageField(color="blue")
    verified = True
    rating = 1.0
