from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=70)


class Portfolio(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=70),
        textfull=RichTextField(_('textfull'))
    )

    category = models.ForeignKey(PortfolioCategory, on_delete=models.PROTECT)
    image = models.ImageField()
    link = models.URLField()
    watches = models.PositiveBigIntegerField(default=0)
    like = models.PositiveBigIntegerField(default=0)


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
    image = models.ImageField()


class PostLike(models.Model):
    post_id = models.PositiveIntegerField()
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"Like on Post {self.post_id} by {self.ip_address}"