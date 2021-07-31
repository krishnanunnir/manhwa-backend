import factory
from web.models import Manhwa, Author, Tags


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class TagsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tags

    name = factory.Faker("word")


class ManhwaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manhwa

    title = factory.Faker("sentence", nb_words=4)
    author = factory.SubFactory(AuthorFactory)
    status = "Ongoing"
    description = factory.Faker("sentence", nb_words=20)
    cover_image = factory.django.ImageField(color="blue")
    verified = True
    rating = 1.0

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            TagsFactory.create_batch(3)
