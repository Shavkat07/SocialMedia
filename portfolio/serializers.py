from rest_framework import serializers
from portfolio.models import Portfolio, PortfolioCategory, PortfolioImage
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField


class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ('id', 'name')


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ('image',)


class PortfolioSerializer(TranslatableModelSerializer):
    category = PortfolioCategorySerializer()
    images = PortfolioImageSerializer(source='portfolioimage_set', many=True)
    translations = TranslatedFieldsField(shared_model=Portfolio)

    class Meta:
        model = Portfolio
        fields = ('id', 'category', 'title', 'image', 'link',
                  'textfull', 'watches', 'like', 'images', 'translations')
