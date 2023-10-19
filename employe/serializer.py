from employe.models import TeamMember
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField


class TeamMemberSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=TeamMember)

    class Meta:
        model = TeamMember
        fields = ('id', 'role', 'image', 'telegram',
                  'instagram', 'linkedin', 'github', 'translations')
