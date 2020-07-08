from django import forms


from MyApp.models import ServiceNameModel, ServiceDurationModel


class CommemorationForm(forms.Form):
    service = forms.ModelChoiceField(
        label='Служба',
        queryset=ServiceNameModel.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None
    )
    duration = forms.ModelChoiceField(
        label='Продолжительность',
        queryset=ServiceDurationModel.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None
    )
    # names_health =
    # names_death =