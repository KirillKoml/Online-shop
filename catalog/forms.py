from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


# Список запрещённых слов в тексте продукта. Включает регистрозависимые и нерегистрозависимые слова.
forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар', 'Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция',
                   'Радар', ]


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'views_counter',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('В тексте продукта есть запрещённое слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('В тексте продукта есть запрещённое слово')
        return cleaned_data

    def clean_price(self):
        cleaned_data = self.cleaned_data['price']

        if cleaned_data <= 0:
            raise forms.ValidationError('Цена не может быть нулевой или отрицательной')

        return cleaned_data
