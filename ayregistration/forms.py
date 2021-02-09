from django import forms
from .models import RegistrantInfo
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RegistrantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'index'
        self.helper.add_input(Submit('submit', 'Enroll'))
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-3 mb-0'),
                Column('last_name', css_class='form-group col-md-3 mb-0'),
                Column('phone_number', css_class='form-group col-md-2 mb-0'),
               Column('grade', css_class='form-group col-md-1 mb-0'),
               Column('church', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
         
            Row(
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-3 mb-0'),
                Column('city', css_class='form-group col-md-2 mb-0'),
                Column('state', css_class='form-group col-md-2 mb-0'),
                Column('zip_code', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),

             Row(
                Column (
                    Row (
                Column('iwaspathfinder', css_class='form-group col-md-4 mb-0'),
                Column('ifyespathfinder', css_class='form-group col-md-4 mb-0'),
                Column('dadismasterguide', css_class='form-group col-md-4 mb-0'),
               

              ),
                Row (
                Column('dadwaspathfinder', css_class='form-group col-md-4 mb-0'),
                Column('momismasterguide', css_class='form-group col-md-4 mb-0'),
                Column('momwaspathfinder', css_class='form-group col-md-4 mb-0'),
                  
              ),


                Column(
                    Row (
                        Column('wishspecialclub', css_class='form-group')
                    )
                )
              
            ))
        )

    class Meta:
        model = RegistrantInfo
        fields = '__all__'