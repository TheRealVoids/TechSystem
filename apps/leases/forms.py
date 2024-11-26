from django import forms


class LeaseRequestForm(forms.Form):
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )
