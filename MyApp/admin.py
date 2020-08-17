from django import forms
from django.contrib import admin
# from django.db import models
from django.utils.safestring import mark_safe

from .models import *


admin.site.site_title = 'Управление сайтом Свято-Троицкого собора'
admin.site.site_header = 'Управление сайтом Свято-Троицкого собора'


@admin.register(HeaderModel)
class HeaderModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    list_display = ('created_dt', 'title', 'get_image')
    list_display_links = ('created_dt', 'title')

    def get_image(self, header_object):
        if header_object.background_image:
            return mark_safe(f'<img src="{header_object.background_image.url}" width="75">')

    get_image.short_description = 'Изображение фона'


class ScheduleEventsForm(forms.ModelForm):
    class Meta:
        model = ScheduleEventsModel
        fields = ['event_time', 'event_text']
        widgets = {
            'event_time': forms.TimeInput(format='%H:%M'),
            'event_text': forms.TextInput(attrs={'style': 'width: 350px;'})
        }


class ScheduleEventInline(admin.TabularInline):
    model = ScheduleEventsModel
    extra = 5
    form = ScheduleEventsForm


@admin.register(ScheduleModel)
class ScheduleModelAdmin(admin.ModelAdmin):
    inlines = [ScheduleEventInline, ]


@admin.register(PhotoSliderModel)
class PhotoSliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'description', 'is_active')
    list_display_links = ('get_image', )
    list_editable = ('description', 'is_active', )

    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')

    get_image.short_description = 'Фотография'


class ParagraphForm(forms.ModelForm):
    class Meta:
        model = ParagraphModel
        fields = ['is_active', 'title', 'text', 'image']


class ParagraphInline(admin.TabularInline):
    model = ParagraphModel
    form = ParagraphForm
    extra = 5
    fields = ('is_active', 'title', 'text', 'image')


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, ]


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Заголовок', {'fields': ('title', 'menu_title')}),
        ('Контакты', {'fields': ('address', 'phone', 'email', 'vkontakte', 'instagram')}),
        ('Карта', {'fields': ('map_code', )}),
    )


class EventParagraphForm(forms.ModelForm):
    class Meta:
        model = EventParagraphModel
        fields = ['title', 'text', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 350px;'}),
            'text': forms.Textarea(attrs={'rows': 5, 'cols': 60})
        }


class EventParagraphInline(admin.TabularInline):
    model = EventParagraphModel
    form = EventParagraphForm
    extra = 3


class EventPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventPhotoForm, self).__init__(*args, **kwargs)

        self.fields['thumbnail'].disabled = True

    class Meta:
        model = EventPhotoModel
        fields = ['photo', 'thumbnail', 'alt']
        widgets = {
            'thumbnail': forms.TextInput()
        }



class EventPhotoInline(admin.TabularInline):
    model = EventPhotoModel
    form = EventPhotoForm
    extra = 9


@admin.register(EventsModel)
class EventsModelAdmin(admin.ModelAdmin):
    inlines = [EventParagraphInline, EventPhotoInline]
    readonly_fields = ('created_dt', )

    fieldsets = (
        ('Настройка статьи', {
            'fields': ('created_dt', 'is_active')
        }),
        ('Описание статьи', {
            'fields': ('title', 'annotation', 'photo', 'date'),
        }),
        ('Ссылка на источник', {
            'fields': ('source', 'source_link'),
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
                           attrs={'rows': 3,
                                  'cols': 80})},
    }