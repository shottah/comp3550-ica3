from django import forms
from django_countries.fields import CountryField
from .person import Person

class PersonForm (forms.ModelForm):
    # Define Input Labels
    fname = forms.CharField(label="First Name", max_length=30)
    lname = forms.CharField(label="Last Name", max_length=30)

    class Meta:
        # Define Model being written to
        model = Person
        # Define fields being set
        fields = (
            'fname',
            'lname',
            'country'
        )

    def save (self, commit=True):
        # Override save() method
        p = Person()
        p.fname = self.cleaned_data['fname']
        p.lname = self.cleaned_data['lname']
        p.country = self.cleaned_data['country']

        if commit:
            p.save()
        
        # Return new Object
        return p