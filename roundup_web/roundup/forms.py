from roundup.models import Organization, BookmarkletKey, Item

from django import forms
from django.contrib.auth.models import User

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ('contributed_date', 'bookmarklet_key')