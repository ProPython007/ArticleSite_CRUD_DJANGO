from typing import Any
from django import forms


from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'name': "title", 'type': "text", 'class': "form-control", 'id': "input_title"}),
            'content': forms.Textarea(attrs={'name':"content", 'class':"form-control", 'id':"input_content", 'rows':"4"}),
        }
    
    def clean(self):
        cleaned_data = self.cleaned_data #dict
        title = cleaned_data.get('title')

        if Article.objects.filter(title=title).exclude(id=self.instance.id).exists():
            self.add_error('title', 'This title is already taken!')
        
        return cleaned_data
    

class ArticleFormOld(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'name': "title", 'type': "text", 'class': "form-control", 'id': "input_title"})
    )
    # title.widget.attrs.update({'name':"title", 'type':"text", 'class':"form-control", 'id':"input_title"})
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={'name':"content", 'class':"form-control", 'id':"input_content", 'rows':"4"})
    )

    def clean_title(self):
        cleaned_data = self.cleaned_data #dict
        title = cleaned_data.get('title')
        titles = Article.objects.filter(title=title)

        if titles:
            raise forms.ValidationError('This title is already taken!')
        
        return title