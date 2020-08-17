from django import forms

from MyApp.models import ServiceNameModel, ServiceDurationModel, NoteModel, NoteNamesModel


class NoteForm(forms.ModelForm):
    service_name = forms.ModelChoiceField(
        label='Служба',
        queryset=ServiceNameModel.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None
    )
    service_duration = forms.ModelChoiceField(
        label='Продолжительность',
        queryset=ServiceDurationModel.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None
    )

    class Meta:
        model = NoteModel
        fields = ('service_name', 'service_duration')


class CustomNamesForm(forms.ModelForm):
    def save(self, commit=True):
        self.cleaned_data['type'] = 'TEST'
        return super(CustomNamesForm, self).save(commit=commit)

    class Meta:
        model = NoteNamesModel
        fields = ('name', )


NoteNamesFormSet = forms.inlineformset_factory(
    parent_model=NoteModel,
    model=NoteNamesModel,
    fields=('name', ),
    extra=5,
    can_delete=False,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
    },
)

