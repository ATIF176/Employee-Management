from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_name', 'mobile', 'emp_code', 'positions') # for selective objects
        labels = {
            'emp_name':'Employee Name',
            'emp_code':'Emp. Code'
        }
        # fields = '__all__' for all objects

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['positions'].empty_label = "select" 
        self.fields['emp_name'].required = True