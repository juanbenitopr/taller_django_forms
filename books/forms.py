from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class BookForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.ChoiceField(choices=[(user.id, user.username) for user in User.objects.all()])
    rating = forms.IntegerField(min_value=0, max_value=5)

    def clean_author(self):
        try:
            author = int(self.cleaned_data.get('author'))
        except ValueError:
            raise ValidationError('The author identifier must be an integer', code='invalid_author')

        if not User.objects.filter(pk=author).exists():
            raise ValidationError('The author must exists', code='invalid_author')

        return author
