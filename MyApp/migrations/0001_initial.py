# Generated by Django 3.0.6 on 2020-06-28 12:25

from django.conf import settings
import django.contrib.auth
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать статью на сайте?')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('changed_dt', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок статьи')),
            ],
            options={
                'verbose_name': 'О соборе :: Статья',
                'verbose_name_plural': 'О соборе :: Статьи',
                'ordering': ['created_dt'],
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Наименование')),
                ('menu_title', models.CharField(blank=True, max_length=255, verbose_name='Наименование для навигации')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Электронная почта')),
                ('vkontakte', models.CharField(blank=True, max_length=100, verbose_name='Группа VKontakte')),
                ('instagram', models.CharField(blank=True, max_length=100, verbose_name='Инстаграм')),
                ('map_code', models.TextField(blank=True, verbose_name='Код для отображения карты')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать статью на сайте?')),
                ('event_date', models.DateField(blank=True, verbose_name='Дата события')),
                ('event_title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок статьи')),
                ('event_annotation', models.CharField(blank=True, help_text='Не более 255 символов', max_length=255, verbose_name='Аннотация к статье')),
                ('event_photo', models.ImageField(blank=True, help_text='Рекомендуемый размер изображения 300 x 200', upload_to='images/events/%Y%m%d/', verbose_name='Изображения для аннотации')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='HeaderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(help_text='Рекомендуемый размер изображения 1280 x 400', upload_to='images/main_page_background/%Y%m%d/', verbose_name='Фотография фона')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
                'ordering': ['-created_dt'],
                'get_latest_by': 'created_dt',
            },
        ),
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записки')),
                ('pay_dt', models.DateTimeField(blank=True, editable=False, verbose_name='Дата оплаты')),
                ('delivery_dt', models.DateTimeField(blank=True, editable=False, verbose_name='Дата доставки записки по e-mail')),
            ],
            options={
                'verbose_name': 'Записка о поминовении',
                'verbose_name_plural': 'Записки о поминовении',
            },
        ),
        migrations.CreateModel(
            name='PhotoCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Индекс сортировки')),
                ('section', models.CharField(choices=[('ID', 'Главная страница'), ('AB', 'О соборе'), ('CM', 'Записки'), ('CN', 'Контакты'), ('EV', 'События'), ('SC', 'Расписание')], default='AB', max_length=2, verbose_name='Раздел сайта')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoSliderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать фотографию на сайте?')),
                ('photo', models.ImageField(upload_to='images/photo_slider/%Y%m%d/', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'О соборе :: Фото-слайдер',
                'verbose_name_plural': 'О соборе :: Фото-слайдер',
            },
        ),
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(db_index=True, verbose_name='Дата')),
                ('header', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='ServiceDurationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_duration_value', models.CharField(db_index=True, max_length=100, verbose_name='Продолжительность службы')),
            ],
            options={
                'verbose_name': 'Длительность поминовения',
            },
        ),
        migrations.CreateModel(
            name='ServiceNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(db_index=True, max_length=150, verbose_name='Название службы')),
            ],
            options={
                'verbose_name': 'Служба',
                'verbose_name_plural': 'Службы',
            },
        ),
        migrations.CreateModel(
            name='ScheduleEventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_time', models.TimeField(verbose_name='Время начала службы')),
                ('event_text', models.CharField(max_length=255, verbose_name='Описание службы')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.ScheduleModel')),
            ],
            options={
                'verbose_name': 'Расписание дня',
                'verbose_name_plural': 'Расписания дней',
            },
        ),
        migrations.CreateModel(
            name='ParagraphModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Параграф виден на сайте?')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_dt', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок параграфа')),
                ('image', models.ImageField(blank=True, upload_to='images/articles/%Y%m%d/', verbose_name='Изображение')),
                ('text', models.TextField(blank=True, verbose_name='Текст параграфа')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.ArticleModel')),
            ],
            options={
                'verbose_name': 'О соборе :: Статья :: Параграф',
                'verbose_name_plural': 'О соборе :: Статья :: Параграфы',
            },
        ),
        migrations.CreateModel(
            name='NoteNamesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('HE', 'О здравии'), ('RE', 'Об упокоении')], max_length=50, verbose_name='Поминовение')),
                ('name', models.CharField(max_length=150, verbose_name='Имя для поминовения')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.NoteModel')),
            ],
            options={
                'verbose_name': 'Имя в записке о поминовении',
                'verbose_name_plural': 'Имена в записках о поминовении',
            },
        ),
        migrations.AddField(
            model_name='notemodel',
            name='service_duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyApp.ServiceDurationModel'),
        ),
        migrations.AddField(
            model_name='notemodel',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyApp.ServiceNameModel'),
        ),
        migrations.CreateModel(
            name='EventPhotoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_photo', models.ImageField(blank=True, help_text='Если не указано, то будет использовано оригиналное изображение', upload_to='images/events/albums/%Y%m%d/', verbose_name='Уменьшенное изображение')),
                ('photo', models.ImageField(upload_to='', verbose_name='Оригинальное изображение')),
                ('alt', models.CharField(help_text='Текст будет отображаться, если у пользователя выключены изображения. Также текст используется поисковыми системами для поиска изображений.', max_length=255, verbose_name='Описание изображения')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.EventsModel')),
            ],
            options={
                'verbose_name': 'Событие :: Статья :: Альбом',
                'verbose_name_plural': 'Событие :: Статья :: Альбомы',
            },
        ),
        migrations.CreateModel(
            name='EventParagraphModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок параграфа')),
                ('photo', models.ImageField(blank=True, upload_to='images/events/paragraphs/%Y%m%d/', verbose_name='Изображение')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.EventsModel')),
            ],
            options={
                'verbose_name': 'Событие :: Статья :: Параграф',
                'verbose_name_plural': 'Событие :: Статья :: Параграфы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('active', models.BooleanField(default=True, verbose_name='Отображать статью на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Индекс сортировки')),
                ('section', models.CharField(choices=[('ID', 'Главная страница'), ('AB', 'О соборе'), ('CM', 'Записки'), ('CN', 'Контакты'), ('EV', 'События'), ('SC', 'Расписание')], default='AB', max_length=2, verbose_name='Раздел сайта')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок статьи')),
                ('text', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Исходное изображение')),
                ('photo_small', models.ImageField(blank=True, upload_to='', verbose_name='Уменьшенное изображение (ширина 200 px)')),
                ('author', models.ForeignKey(on_delete=models.SET(django.contrib.auth.get_user_model), to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи')),
            ],
        ),
    ]
