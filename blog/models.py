from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class BlogCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Blog(TranslatableModel):

    translations = TranslatedFields(
        title=models.CharField(_("Title"),max_length=120),
        text=models.TextField(_("text"),max_length=5000)
    )

    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)
    image = models.ImageField()
    created = models.DateField(auto_now_add=True)
    watches = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
