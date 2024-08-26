from django import forms

class UserInputForm(forms.Form):
    userinput = forms.CharField(label="User Input",widget=forms.TextInput(attrs={
        'class': 'appearance-none block bg-gray-900 text-white rounded py-3 px-4 mb-3 w-100 focus:outline-none ',
        'placeholder': 'Enter your query'
        }))

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                
                label=f"{question.id}. {question.text}",
                choices=[(answer.id, answer.text) for answer in question.answer_set.all()],
                widget=forms.RadioSelect(attrs={
                    'class':'ml-8 bg-black text-gray-600 border-gray-300     '
                })
            )
