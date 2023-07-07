from django import forms
from .models import ProfileModel,FruitModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class FruitBaseModel(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'



class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': False,
            'last_name': False,
            'email': False,
            'password': False
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']

        first_name=forms.CharField(label='First Name')
        last_name=forms.Field(label='Last Name')
        image_url=forms.URLField(label='Image URL')
        age=forms.IntegerField(label='Age')



class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields ='__all__'
        labels = {
            'name': False,
            'image_url': False,
            'description': False,
            'nutrition': False
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'})
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition'
        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = ['name', 'description', 'image_url']
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

