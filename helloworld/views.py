from django.http import HttpResponse
from django.shortcuts import render
from forms import ZipcodeForm
import zipcode as zp


def main(request):
    return HttpResponse("Hello World!!")


def index(request):
    if request.method == 'POST':
        f = ZipcodeForm(request.POST)
        if f.is_valid():
            zipcode = int(f.cleaned_data['number'])
            state = zp.get_state(zipcode)
    else:
        f = ZipcodeForm()
        state = ''
    return render(request, 'index.html',
                      {'zipcode_form': f, 'state': state})
