from django import forms

from careers.models import JobApplication


class JobApplicationForm(forms.ModelForm):
    """
    A form for JobApplication model
    """
    class Meta:
        model = JobApplication
