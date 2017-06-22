from django.contrib import admin
from eventex.core.models import Speaker, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return f'<a href="{obj.website}">{obj.website}</a>'

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return f'<img width="32px" src="{obj.photo}" />'

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

admin.site.register(Speaker, SpeakerModelAdmin)
