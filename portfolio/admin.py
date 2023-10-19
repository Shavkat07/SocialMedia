from django.contrib import admin
from portfolio.models import Portfolio, PortfolioCategory, PortfolioImage
from parler.admin import TranslatableAdmin
from django.contrib.sessions.models import Session

class PortfolioAdmin(TranslatableAdmin):
    list_display = ('id', 'title', 'category', 'watches', 'like')
    list_display_links = ('id', 'title', 'category')
    fieldsets = (
        (None, {
            'fields': ('title', 'textfull', 'category',
                       "image", 'link', 'watches', 'like'),
        }),
    )


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register([PortfolioCategory, PortfolioImage, Session])
