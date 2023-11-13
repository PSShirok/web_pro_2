from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        clean_name = self.cleaned_data['name']

        if clean_name.lower() in ['казино', 'криптовалюта',
                                        'крипта', 'биржа', 'дешево',
                                        'бесплатно', 'обман',
                                        'полиция', 'радар']:
            raise forms.ValidationError('Это запрещено продавать')
        return clean_name

    def clean_text(self):
        clean_text = self.cleaned_data['text']

        if clean_text.lower() in ['казино', 'криптовалюта',
                                        'крипта', 'биржа', 'дешево',
                                        'бесплатно', 'обман',
                                        'полиция', 'радар']:
            raise forms.ValidationError('Это запрещено продавать')
        return clean_text