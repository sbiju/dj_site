from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]


class ContactusForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField()
    message = forms.CharField()
