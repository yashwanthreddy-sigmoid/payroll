from django.forms import ModelForm
from .models import Employee , Users, Role, Accountdetails,Emprole

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = "__all__"

class AccountForm(ModelForm):
    class Meta:
        model = Accountdetails
        fields = "__all__"

class EmpRoleForm(ModelForm):
    class Meta:
        model = Emprole
        fields="__all__"
