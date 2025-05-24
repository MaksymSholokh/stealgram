from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ['text', 'photo', 'video']  

    def save(self, commit=True): 
        post = super().save(commit=False) 
        if commit: 
            post.status = 'Pb'  
            post.save()
        return post


class CommentForm(forms.Form): 
    text = forms.CharField(widget=forms.Textarea())