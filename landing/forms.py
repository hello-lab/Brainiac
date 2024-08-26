from django import forms
class RegisterUser(forms.Form):
    
    SUBJECT_CHOICES = (
    ("1", "Physics"),
    ("2", "Mathematics"),
    ("3", "Chemistry"),
    ("4", "Digital Marketing"),
    ("5", "Biology"),
    ("6", "Computer Science"),
    ("7", "History"),
    ("8", "Geography"),
    ("9", "English Literature"),
    ("10", "Economics"),
    ("11", "Psychology"),
    ("12", "Sociology"),
    ("13", "Philosophy"),
    ("14", "Political Science"),
    ("15", "Statistics"),
    ("16", "Environmental Science"),
    ("17", "Engineering"),
    ("18", "Business Administration"),
    ("19", "Accounting"),
    ("20", "Finance"),
    ("21", "Marketing"),
    ("22", "Entrepreneurship"),
    ("23", "Law"),
    ("24", "Medicine"),
    ("25", "Nursing"),
    ("26", "Education"),
    ("27", "Art"),
    ("28", "Music"),
    ("29", "Theatre"),
    ("30", "Film Studies"),
    ("31", "Journalism"),
    ("32", "Communications"),
    ("33", "Anthropology"),
    ("34", "Archaeology"),
    ("35", "Linguistics"),
    ("36", "Foreign Languages"),
    ("37", "Astronomy"),
    ("38", "Astrophysics"),
    ("39", "Geology"),
    ("40", "Oceanography"),
    ("41", "Meteorology"),
    ("42", "Agriculture"),
    ("43", "Horticulture"),
    ("44", "Veterinary Science"),
    ("45", "Public Health"),
    ("46", "Sports Science"),
    ("47", "Graphic Design"),
    ("48", "Interior Design"),
    ("49", "Fashion Design"),
    ("50", "Culinary Arts"),
)
    
    name = forms.CharField(label=" Name",widget=forms.TextInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter your name'
        }),max_length=200)
    email = forms.CharField(label=" Email",widget=forms.EmailInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter your email'
        }),max_length=200)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter a password (Choose a strong one!)'
        }),max_length=200)
    institution = forms.CharField(label="Institution",widget=forms.TextInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter your Institution name'
        }),max_length=200)
    subjects=forms.CharField(label="Subjects (seperated by commas)",widget=forms.TextInput(attrs=
                                                                                            {
        'class': 'form-control bg-gray-900 border-black min-h-12 focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter list of subjects (seperated by commas)'
                                                                                            }))
    
    
class LoginUser(forms.Form):
    name = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter your name'
    }),max_length=200)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-gray-900 border-black focus:bg-gray-800 focus:text-white text-gray-300',
        'placeholder': 'Enter your password'
    }),max_length=200)
    