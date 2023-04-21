from django import forms
from .models import Todo

class Contact_Form(forms.ModelForm):
    class Meta():

        model = Todo
        fields = ("title", "description", "deadline")
        labels = {"title":"タイトル",
                  "description":"詳細を記入(空白可)",
                  "deadline":"yyyy-mm-dd(要入力)"
                }
