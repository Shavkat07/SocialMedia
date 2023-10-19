from django.contrib import admin

from employe.models import TeamMember
from parler.admin import TranslatableAdmin


class TeamMemberAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'role')
    list_display_links = ('id', 'name', 'role')
    fieldsets = (
        (None, {
            'fields': ('name', 'about', 'role', "image",
                       "telegram", 'instagram', 'linkedin', 'github'),
        }),
    )


admin.site.register(TeamMember, TeamMemberAdmin)

