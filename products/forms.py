from Django import forms
from .models import Product, Category


def ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init_-(*args, **kwargs)