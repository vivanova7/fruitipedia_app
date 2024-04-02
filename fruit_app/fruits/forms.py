from django import forms

from fruit_app.fruits.models import Fruit


class BaseClassFruitForm(forms.ModelForm):

    class Meta:
        model = Fruit

        exclude = ('owner',)


class CreateFruitForm(BaseClassFruitForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)
        widgets = {
            'fruit_name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'fruit_image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition_info': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }

        labels = {
            'fruit_name': '',
            'fruit_image_url': '',
            'description': '',
            'nutrition_info': '',
        }

        error_messages = {
            'fruit_name': {
                'unique': "This fruit name is already in use! Try a new one.",
            }
        }


