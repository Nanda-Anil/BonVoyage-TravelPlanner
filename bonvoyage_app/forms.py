from django import forms

class userregform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)

class userlogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class agencyregform(forms.Form):
    agency = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)

class agencylogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class uploadform(forms.Form):
    agency=forms.CharField(max_length=20)
    email = forms.EmailField()
    state= forms.CharField(max_length=20)
    spots=forms.CharField(max_length=300)
    food= forms.CharField(max_length=20)
    pet = forms.CharField(max_length=20)
    duration = forms.CharField(max_length=20)
    cab=forms.CharField(max_length=20)
    stay = forms.CharField(max_length=20)
    rate = forms.CharField(max_length=20)

class bookform(forms.Form):
    agency=forms.CharField(max_length=20)
    state=forms.CharField(max_length=20)
    spots = forms.CharField(max_length=500)
    rate = forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)
    frmdy = forms.CharField(max_length=20)
    tody = forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.CharField(max_length=20)

class confirmationemailform(forms.Form):
    agency=forms.CharField(max_length=20)
    email=forms.EmailField()
