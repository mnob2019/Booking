from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .models import Record,Book
from .forms import RecordForm, BookForm
from django.contrib.contenttypes.models import ContentType
from geopy.geocoders import Nominatim

#add for DRF API to work
from rest_framework import generics
from .serializers import RecordSerializer

geolocator = Nominatim()

#View to see all points
def record_map(request):

	return render(request, "home.html")

#create a new location
def create_record(request):
	form = RecordForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		#get coordinates
		location = geolocator.geocode(instance.location)
		instance.latitude = location.latitude
		instance.longitude = location.longitude
		instance.save()
		return HttpResponseRedirect('/')

	context = {
        "form":form
	}

	return render(request, "record/create.html", context)

#API to get all records
class RecordAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

def book(request):
	form = BookForm(request.POST or None)

	if form.is_valid():
		booking = Book(
		#get coordinates
		 name = form.cleaned_data['name'],
         email = form.cleaned_data['email'],
         phonenumber = form.cleaned_data['phonenumber'],)

		booking.save()
		return HttpResponseRedirect('/')

	context = {
        "form":form
	}

	return render(request, "record/book.html", context)
