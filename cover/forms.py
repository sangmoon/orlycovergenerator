from django import forms
from urllib.parse import urlencode
from .utils import COLOR_CODES


class CoverForm(forms.Form):
    COLOR_CHOICES = [(i, str(COLOR_CODES[i])) for i in range(len(COLOR_CODES))]

    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()
    animal_code = forms.ChoiceField(choices=[(i, i) for i in range(1, 41)])
    color_code = forms.ChoiceField(choices=COLOR_CHOICES)
    guide_text = forms.CharField()
    guide_text_placement = forms.ChoiceField(
        choices=[
            ('botoom_right', 'botoom_right'),
            ('bottom_left', 'bottom_left'),
            ('top_right', 'top_right'),
            ('top_left', 'top_left'),
        ]
    )

    @property
    def get_params(self):
        if hasattr(self, "cleaned_data"):
            return urlencode(self.cleaned_data)
        else:
            return None
