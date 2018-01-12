from django import forms
from .models import Comments


# форма для добавления комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=['comments_text']

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(CommentForm, self).__init__(request, *args, **kwargs)

        self.fields['comments_text'].widget.attrs.update(
            {'class': 'form-control'})

