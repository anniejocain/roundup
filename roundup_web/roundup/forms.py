from roundup.models import Organization, BookmarkletKey, Item

from django import forms
from django.contrib.auth.models import User

class AddItemForm(forms.ModelForm):
    
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'maxlength':117}))

    class Meta:
        model = Item
        exclude = ('contributed_date', 'bookmarklet_key')