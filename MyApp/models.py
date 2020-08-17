from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image
import os
import io

from date_to_string_rus import date_to_string_rus
from date_to_day_of_week_rus import date_to_day_of_week_rus


INDEX = 'ID'
ABOUT = 'AB'
COMMEMORATION = 'CM'
CONTACTS = 'CN'
EVENTS = 'EV'
SCHEDULE = 'SC'
SECTIONS = [
    (INDEX, 'Главная страница'),
    (ABOUT, 'О соборе'),
    (COMMEMORATION, 'Записки'),
    (CONTACTS, 'Контакты'),
    (EVENTS, 'События'),
    (SCHEDULE, 'Расписание'),
]


# class Article(models.Model):
#     author = models.ForeignKey(verbose_name='Автор статьи', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_user_model), blank=False)
#     create_date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
#     active = models.BooleanField(verbose_name='Отображать статью на сайте', default=True)
#     order = models.PositiveSmallIntegerField(verbose_name='Индекс сортировки', default=0)
#
#     section = models.CharField('Раздел сайта', max_length=2, choices=SECTIONS, default=ABOUT, blank=False)
#     title = models.CharField('Заголовок статьи', max_length=200, blank=True)
#     text = models.TextField('Текст статьи', blank=True)
#     photo = models.ImageField('Исходное изображение', blank=True)
#     photo_small = models.ImageField('Уменьшенное изображение (ширина 200 px)', blank=True)
#
#     def __str__(self):
#         return self.title
#
#     def get_sentinel_user(self):
#         return get_user_model().objects.get_or_create(username='deleted')[0]


# class PhotoCarousel(models.Model):
#     active = models.BooleanField(verbose_name='Отображать на сайте', default=True)
#     order = models.PositiveSmallIntegerField(verbose_name='Индекс сортировки', default=0)
#     section = models.CharField('Раздел сайта', max_length=2, choices=SECTIONS, default=ABOUT, blank=False)
#     photo = models.ImageField('Изображение', blank=True)


class HeaderModel(models.Model):
    background_image = models.ImageField(upload_to='images/main_page_background/%Y%m%d/',
                                         verbose_name='Фотография фона',
                                         help_text='Рекомендуемый размер изображения 1280 x 400')
    title = models.CharField(max_length=150, verbose_name='Заголовок', blank=True)
    text = models.TextField(verbose_name='Текст', blank=True)
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
        ordering = ['-created_dt']
        get_latest_by = 'created_dt'


class PhotoSliderModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Отображать фотографию на сайте?')
    photo = models.ImageField(upload_to='images/photo_slider/%Y%m%d/', verbose_name='Изображение')
    description = models.CharField(max_length=255, verbose_name='Подпись', blank=True)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = 'О соборе :: Фото-слайдер'
        verbose_name_plural = 'О соборе :: Фото-слайдер'


class ScheduleModel(models.Model):
    event_date = models.DateField(verbose_name='Дата', db_index=True)
    header = models.CharField(max_length=150, verbose_name='Заголовок', blank=True)

    @property
    def day_of_week(self):
        return date_to_day_of_week_rus(self.event_date).title()

    def __str__(self):
        return date_to_string_rus(self.event_date) + ' - ' + str(self.header)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class ScheduleEventsModel(models.Model):
    schedule = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE)
    event_time = models.TimeField(verbose_name='Время начала службы')
    event_text = models.CharField(max_length=255, verbose_name='Описание службы')

    def __str__(self):
        return str(self.event_time) + ' - ' + str(self.event_text)

    class Meta:
        verbose_name = 'Расписание дня'
        verbose_name_plural = 'Расписания дней'


class ArticleModel(models.Model):
    is_active = models.BooleanField(verbose_name='Отображать статью на сайте?', default=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    changed_dt = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, verbose_name='Заголовок статьи', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О соборе :: Статья'
        verbose_name_plural = 'О соборе :: Статьи'
        ordering = ['created_dt']


class ParagraphModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Параграф виден на сайте?')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_dt = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    article = models.ForeignKey(to=ArticleModel, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name='Заголовок параграфа', blank=True)
    image = models.ImageField(upload_to='images/articles/%Y%m%d/', verbose_name='Изображение', blank=True)
    text = models.TextField(verbose_name='Текст параграфа', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О соборе :: Статья :: Параграф'
        verbose_name_plural = 'О соборе :: Статья :: Параграфы'


class ServiceNameModel(models.Model):
    service_name = models.CharField(max_length=150, verbose_name='Название службы', db_index=True)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Служба'
        verbose_name_plural = 'Службы'


class ServiceDurationModel(models.Model):
    service_duration_value = models.CharField(max_length=100, verbose_name='Продолжительность поминовения', db_index=True)

    def __str__(self):
        return self.service_duration_value

    class Meta:
        verbose_name = 'Продолжительность поминовения'
        verbose_name_plural = 'Продолжительность поминовений'


class NoteModel(models.Model):
    service_name = models.ForeignKey(to=ServiceNameModel, on_delete=models.PROTECT)
    service_duration = models.ForeignKey(to=ServiceDurationModel, on_delete=models.PROTECT)
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записки')
    pay_dt = models.DateTimeField(editable=False, verbose_name='Дата оплаты', blank=True, null=True)
    delivery_dt = models.DateTimeField(editable=False, verbose_name='Дата доставки записки по e-mail', blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Записка о поминовении'
        verbose_name_plural = 'Записки о поминовении'


class NoteNamesModel(models.Model):
    HEALTH = 'HE'
    REPOSE = 'RE'
    COMMEMORATION_TYPES = [
        (HEALTH, 'О здравии'),
        (REPOSE, 'Об упокоении'),
    ]

    note_id = models.ForeignKey(to=NoteModel, on_delete=models.CASCADE)

    type = models.CharField(max_length=50, choices=COMMEMORATION_TYPES, verbose_name='Поминовение')
    name = models.CharField(max_length=150, verbose_name='Имя для поминовения')

    def __str__(self):
        return self.type + ' ' + self.name

    class Meta:
        verbose_name = 'Имя в записке о поминовении'
        verbose_name_plural = 'Имена в записках о поминовении'


class ContactModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True)
    menu_title = models.CharField(max_length=255, verbose_name='Наименование для навигации', blank=True)
    # photo = models.ImageField(upload_to='images/contacts/%Y%m%d/', verbose_name='Фотография', blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Электронная почта', blank=True)
    vkontakte = models.CharField(max_length=100, verbose_name='Группа VKontakte', blank=True)
    instagram = models.CharField(max_length=100, verbose_name='Инстаграм', blank=True)
    map_code = models.TextField(verbose_name='Код для отображения карты', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['pk']


class EventsModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Отображать статью на сайте?')

    date = models.DateField(verbose_name='Дата события', blank=True)
    source = models.CharField(max_length=255, verbose_name='Оригинал статьи', blank=True)
    source_link = models.CharField(max_length=255,
                                   verbose_name='URL-ссылка на оригинал статьи',
                                   blank=True,
                                   help_text='Ссылка указывается в формате http://www.address.com/some-page.html')
    title = models.CharField(max_length=255, verbose_name='Заголовок статьи', blank=True)
    annotation = models.TextField(verbose_name='Аннотация к статье', blank=True)
    photo = models.ImageField(upload_to='images/events/%Y%m%d/',
                                    verbose_name='Файл изображения',
                                    help_text='Рекомендуемый размер изображения 300 x 200',
                                    blank=True)

    def __str__(self):
        return "[{0}] {1}".format(self.date, self.title)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class EventParagraphModel(models.Model):
    event = models.ForeignKey(to=EventsModel, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name='Заголовок параграфа', blank=True)
    photo = models.ImageField(upload_to='images/events/paragraphs/%Y%m%d/', verbose_name='Изображение', blank=True)
    text = models.TextField(verbose_name='Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие :: Статья :: Параграф'
        verbose_name_plural = 'Событие :: Статья :: Параграфы'


def event_photo_path(instance, filename):
    return 'images/events/event_{0}/{1}'.format(instance.event.pk, filename)


def create_thumbnail(image, thumbnail):
    if not image:
        return

    thumbnail_size = (600, 450)     # Set our max thumbnail size in a tuple (max width, max height)
    thumbnail_name = '_small'.join(os.path.splitext(image.name))    # Make thumbnail name from original photo name

    content_type = image.file.content_type
    data_type, image_type = content_type.split('/')

    # Open original photo which we want to thumbnail using PIL's Image
    thumbnail_image = Image.open(io.BytesIO(image.read()))

    # Turn original photo into thumbnail
    thumbnail_image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # Save the thumbnail
    handle = io.BytesIO()
    thumbnail_image.save(handle, image_type)
    handle.seek(0)

    # Save image to a SimpleUploadedFile which can be saved into ImageField
    suf = SimpleUploadedFile(name=thumbnail_name, content=handle.read(), content_type=content_type)

    # Save SimpleUploadedFile into image field
    thumbnail.save(thumbnail_name, suf, save=False)


class EventPhotoModel(models.Model):
    event = models.ForeignKey(to=EventsModel, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Оригинальное изображение',
                              upload_to=event_photo_path)
    thumbnail = models.ImageField(verbose_name='Уменьшенное изображение',
                                    help_text='Формируется автоматически из оригинального изображения',
                                    upload_to=event_photo_path,
                                    blank=True)
    alt = models.CharField(verbose_name='Описание изображения',
                           max_length=255,
                           help_text='Текст будет отображаться, если у пользователя выключены изображения. '
                                     'Также текст используется поисковыми системами для поиска изображений.',
                           blank=True)

    def save(self, *args, **kwargs):
        if self.photo:
            create_thumbnail(self.photo, self.thumbnail)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Событие :: Статья :: Фотография'
        verbose_name_plural = 'Событие :: Статья :: Фотографии'
