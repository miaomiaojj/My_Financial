from django import forms

education= [
    ('Diploma', 'Diploma'),
    ('Degree', 'Degree'),
    ('Master', 'Master'),
    ('PHD', 'PHD'),
    ('other', 'other'),

    ]

location= [
    ('Singapore', 'Singapore'),
    ('London', 'London'),
    ('other', 'other'),

    ]

houseInfo= [
    ('rent', 'rent'),
    ('House owner', 'House owner'),

    ]

Maritalstatus= [
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Singel', 'Singel'),
    ('Widowed', 'Widowed'),
    ('other', 'other'),

    ]
Occupation= [
    ('employee', 'employee'),
    ('self-employed', 'self-employed'),
    ('worker', 'worker'),

    ('other', 'other'),

    ]
class CHOICES(forms.Form):
    education = forms.CharField(widget=forms.RadioSelect(choices=education))
    location = forms.CharField(widget=forms.RadioSelect(choices=location))
    houseInfo = forms.CharField(widget=forms.RadioSelect(choices=houseInfo))
    Maritalstatus = forms.CharField(widget=forms.RadioSelect(choices=Maritalstatus))
    Occupation = forms.CharField(widget=forms.RadioSelect(choices=Occupation))



