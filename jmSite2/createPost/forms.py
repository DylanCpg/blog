from django import forms


class createPost(forms.Form):
    title=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
    category=forms.ChoiceField(choices=[('cat1','cat1'),('cat2','cat2')])
    image=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
