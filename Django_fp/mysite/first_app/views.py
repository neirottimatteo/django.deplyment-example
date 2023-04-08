from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, Topic, AccesRecord
from . import forms
# Create your views here.

def index(request):
    #MTV
    webpages_list= AccesRecord.objects.order_by('date') # prendi i webpage obkects and order them for date
    date_dict ={'acces_records':webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

    #indice (now it's not working)
    my_dict={'insert_me':'now i  am coming from..'}
    return render(request,'first_app/index.html', context=my_dict)

def form_name_view(request):
    form=forms.FormName()
    if request.method== 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            #do something code
            print('validation succes')
            print("name: "+form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request,'first_app/forms.html',{'form':form})

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative_url_templates.html')