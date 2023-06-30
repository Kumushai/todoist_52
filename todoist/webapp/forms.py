from django import forms
from django.forms import widgets

from webapp.models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["content", "status", "details", "created_at"]
        widgets = {"details": widgets.Textarea(attrs={"cols": 30, "rows": 7}),
                   "created_at": widgets.DateInput(attrs={"type": "date"})}
        error_messages = {"title": {"required": "Поле обязательное"}}

