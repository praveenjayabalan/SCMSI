from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile
from course.models import CourseMaster
from django.conf import settings


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

# class CourseForm(forms.Form):
#     course = forms.ModelChoiceField(queryset = CourseMaster.objects.all() )
#     class Meta:
#         model=CourseMaster

class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        if self.instance.pk:             
            self.fields['consulting_date'].widget.attrs['disabled']=True   
            self.fields['is_fee_paid'].widget.attrs['disabled']=True             
            self.initial.update({'courses': self.instance.course.pk})

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    phone = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'please enter valid number'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    twelth_percentage = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'please enter valid number'}))
    consulting_date = forms.DateField(required=False,
    widget=forms.SelectDateWidget( attrs={'style': 'width: 33%; display: inline-block;'}, empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    is_approved =  forms.BooleanField(required = False,widget=forms.TextInput(attrs={'class':'form-control' ,   'readonly':'readonly'}))
    is_fee_paid =  forms.BooleanField(required = False)
    twelth_marksheet = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),required=False)
    tenth_marksheet = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),required=False)
    courses = forms.ModelChoiceField(
        queryset=CourseMaster.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Select Courses',
        # widget = forms.NumberInput,
        help_text="Enter the alt of the sample",
        to_field_name='id'
    )   

        
    class Meta:
        model = Profile
        fields = ['avatar', 'bio','phone','address','twelth_percentage','consulting_date','is_approved','courses','twelth_marksheet','tenth_marksheet','is_fee_paid']
