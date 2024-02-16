from django import forms
class IMG(forms.Form):
    IMG=forms.ImageField(label="select an image")
    text=forms.CharField(label="ask about this image",widget=forms.Textarea)