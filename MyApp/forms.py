from django import forms


from MyApp.models import ServiceNameModel, ServiceDurationModel, NoteModel, NoteNamesModel


# class CommemorationForm(forms.Form):
#     service = forms.ModelChoiceField(
#         label='Служба',
#         queryset=ServiceNameModel.objects.all(),
#         widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
#         empty_label=None
#     )
#     duration = forms.ModelChoiceField(
#         label='Продолжительность',
#         queryset=ServiceDurationModel.objects.all(),
#         widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
#         empty_label=None
#     )


# class ServiceNameForm(forms.ModelForm):
#     class Meta:
#         model = ServiceNameModel
#         fields = '__all__'
#
#
# class ServiceDurationForm(forms.ModelForm):
#     class Meta:
#         model = ServiceDurationModel
#         fields = '__all__'


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


# class CustomInlineFormSet(forms.models.BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#
#         print('CustomInlineFormset clean:')
#         for form in self.forms:
#             if form.cleaned_data.get('name'):
#                 form.cleaned_data['type'] = NoteNamesModel.HEALTH
#             print('\tCleaned data:', form.cleaned_data)


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
    # fields=('name', 'type'),
    # form=CustomNamesForm,
    extra=5,
    can_delete=False,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        # 'type': forms.HiddenInput(),
    },
    # formset=CustomInlineFormSet
)

