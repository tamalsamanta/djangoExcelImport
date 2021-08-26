from django.shortcuts import render
from tablib import Dataset
from .models import Person
from .resources import PersonResource
from tablib import Dataset
from django.contrib import messages

# Create your views here.
def simple_upload(request):
  if request.method == 'POST':
    person_resource = PersonResource()
    dataset = Dataset()
    newperson = request.FILES['myfile']

    if not newperson.name.endswith('xlsx'):
      messages.info(request, "Wrong Format")
      return render(request, 'upload.html')

    imported_data = dataset.load(newperson.read(), format='xlsx')
    for data in imported_data:
      value = Person(
        data[0],
        data[1],
        data[2],
        data[3]
      )
      value.save()
  return render(request, 'upload.html')