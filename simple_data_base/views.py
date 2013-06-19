# Create your views here.
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from models import Person, Share, Featured

def my_serialize(data):
    xml = render_to_string('xml_template.xml', {'data': data})
    return xml

def graph_it(request):
    data={}
    contributor=User.objects.get(username="rafirosenberg")
    data["contributor"]=contributor
    contributions=contributor.person_added_by.all()
    data['contributions']=contributions
    data= my_serialize(data)
    return render(request, 'relate/graph_example.html',{'data':data})
    