from django import forms

from .models import Ad, Company, Comment


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'text', 'company',)


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'address', 'phone', 'logo',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'post',)