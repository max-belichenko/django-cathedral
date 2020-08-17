import smtplib

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse

from datetime import date, timedelta, datetime

from MyApp.models import *
from MyApp.forms import *


class MainView(TemplateView):
    template_name = 'MyApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['header'] = HeaderModel.objects.latest('pk')    # The latest record with header will be shown on the page.
        context['today'] = date.today()

        # Get schedule 2 days befor and 7 days after today.
        days_before = 2
        days_after = 7
        context['schedule'] = ScheduleModel.objects.filter(
                                                event_date__gte=date.today()-timedelta(days_before)
                                        ).filter(
                                                event_date__lte=date.today()+timedelta(days_after)
                                        )
        context['schedule_events'] = ScheduleEventsModel.objects.filter(schedule_id__in=context['schedule'])
        return context


class AboutView(TemplateView):
    template_name = 'MyApp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photo_slider'] = PhotoSliderModel.objects.filter(is_active__exact=True)
        context['articles'] = ArticleModel.objects.filter(is_active__exact=True)
        context['paragraphs'] = ParagraphModel.objects.filter(article__in=context['articles'])
        return context


class ContactView(TemplateView):
    template_name = 'MyApp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['contacts'] = ContactModel.objects.all()
        return context


class ScheduleView(MainView):
    template_name = 'MyApp/schedule.html'


class EventsView(TemplateView):
    template_name = 'MyApp/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['events'] = EventsModel.objects.filter(is_active__exact=True).order_by('-date')
        return context


class EventDetailView(DetailView):
    model = EventsModel
    context_object_name = 'event'
    template_name = 'MyApp/event_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['paragraphs'] = EventParagraphModel.objects.filter(event__exact=self.kwargs['pk'])
        context['photos'] = EventPhotoModel.objects.filter(event__exact=self.kwargs['pk'])

        return context


def event_view(request, pk):
    event = get_object_or_404(EventsModel, pk=pk)
    return render(request, 'MyApp/event_view.html', {'event': event})


def commemoration(request):
    note = NoteModel()
    health_prefix = 'health'
    repose_prefix = 'repose'

    if request.method == 'POST':
        # Создать экземпляр формы NoteForm и заполнить данными из POST-запроса
        note_form = NoteForm(data=request.POST, instance=note)

        if note_form.is_valid():
            # Сохранить корректно заполненную форму в базе данных
            note_instance = note_form.save()

            # Создать формсет для хранения имён с префиксом 'health' и заполнить его данными из POST-запроса
            health_formset = NoteNamesFormSet(
                data=request.POST,
                files=request.FILES,
                prefix='health',
                instance=note_instance,
            )

            # Создать формсет для хранения имён с префиксом 'repose' и заполнить его данными из POST-запроса
            repose_formset = NoteNamesFormSet(
                data=request.POST,
                files=request.FILES,
                prefix='repose',
                instance=note_instance,
            )

            if health_formset.is_valid():
                for form in health_formset.forms:
                    form.instance.type = NoteNamesModel.HEALTH  # Заполнить поле 'type' значением константы HEALTH
                health_formset.save()   # Сохранить корректно заполненный формсет с префиксом 'health'
            else:
                raise ValidationError(health_formset.errors)
            if repose_formset.is_valid():
                for form in repose_formset.forms:
                    form.instance.type = NoteNamesModel.REPOSE  # Заполнить поле 'type' значением константы REPOSE
                repose_formset.save()   # Сохранить корректно заполненный формсет с префиксом 'repose'
            else:
                raise ValidationError(repose_formset.errors)

            # Отправить данные формы и обоих формсетов на e-mail администратора

            service_name = note_form.cleaned_data['service_name']
            service_duration = note_form.cleaned_data['service_duration']
            health_names = [form.cleaned_data['name'] for form in health_formset if form.cleaned_data.get('name')]
            repose_names = [form.cleaned_data['name'] for form in repose_formset if form.cleaned_data.get('name')]

            subject = f'{service_name} - {service_duration}'
            text = f'<h1>{service_name} - {service_duration}</h1>'
            text += '<h3>О здравии:</h3> <ul>'
            for name in health_names:
                text += f'<li>{name}</li>'
            text += '</ul>'
            text += '<h3>Об упокоении:</h3> <ul>'
            for name in repose_names:
                text += f'<li>{name}</li>'
            text += '</ul> <hr>'

            try:
                send_mail(
                    subject=subject,
                    message=text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_TO_EMAIL, ],
                    fail_silently=False,
                    html_message=text,
                )
            except smtplib.SMTPException as E:
                raise E
            else:
                note_instance.delivery_dt = datetime.now()
                note_instance.save()
        else:
            raise ValidationError(note_form.errors)

        return HttpResponseRedirect(reverse('comm_success'))
    else:
        context = {
            'note_form': NoteForm(instance=note),
            'health_formset': NoteNamesFormSet(prefix=health_prefix, instance=note),
            'repose_formset': NoteNamesFormSet(prefix=repose_prefix, instance=note)
        }

    return render(request, template_name="MyApp/commemorations.html", context=context)


def comm_success(request):
    return render(request, 'MyApp/success.html')

