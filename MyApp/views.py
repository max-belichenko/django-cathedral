from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from datetime import date, timedelta

from MyApp.models import *
from MyApp.forms import CommemorationForm


class MainView(TemplateView):
    template_name = 'MyApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['header'] = HeaderModel.objects.latest('pk')
        context['today'] = date.today()
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
    # pk_url_kwarg = "event_id"
    template_name = 'MyApp/event_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['paragraphs'] = EventParagraphModel.objects.filter(event__exact=self.kwargs['pk'])
        context['photos'] = EventPhotoModel.objects.filter(event__exact=self.kwargs['pk'])

        return context


def event_view(request, pk):
    event = get_object_or_404(EventsModel, pk=pk)
    return render(request, 'MyApp/event_view.html', {'event': event})


# def index(request):
#     return render(request, 'MyApp/index.html')
#
#
# def about(request):
#     articles = Article.objects.filter(section__exact='AB').filter(active__exact=True).order_by('create_date').order_by('order')
#     photocarousel = PhotoCarousel.objects.filter(section__exact='AB').filter(active__exact=True)
#     return render(request, 'MyApp/about.html', {'articles': articles, 'photos': photocarousel})
#
#
# def about_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'MyApp/about.html', {'article': article})


def commemoration(request):
    if request.method == 'POST':
        pass
    else:
        form = CommemorationForm()

    return render(request, 'MyApp/commemoration.html', {'form': form})


# def contacts(request):
#     return render(request, 'MyApp/contacts.html')
#
#
# def events(request):
#     return render(request, 'MyApp/events.html')
#
#
# def events_article(request):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'MyApp/events.html', {'article': article})
#
#
# def schedule(request):
#     return render(request, 'MyApp/schedule.html')
