from .models import PhoneBook

from bootstrap_modal_forms.forms import BSModalModelForm

class PhoneBookModelForm(BSModalModelForm):
    class Meta:
        model = PhoneBook
        fields = ['name','last_name','phone','address','email','note']




