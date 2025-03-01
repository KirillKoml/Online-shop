
from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В названии продукта есть запрещённое слово')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В описании продукта есть запрещённое слово')

        return cleaned_data

    def clean_price(self):
        cleaned_data = self.cleaned_data['price']

        if cleaned_data <= 0:
            raise forms.ValidationError('Цена не может быть нулевой или отрицательной')

        return cleaned_data

class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"