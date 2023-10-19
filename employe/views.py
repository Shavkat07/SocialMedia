from rest_framework.viewsets import ReadOnlyModelViewSet

from employe.models import TeamMember
from employe.serializer import TeamMemberSerializer


class TeamMemberView(ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
