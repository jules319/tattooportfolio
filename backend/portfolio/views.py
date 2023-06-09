from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArtistSerializer, AboutSerializer, TattooSerializer, TestimonialSerializer, BookingSubmissionSerializer
from .models import Artist, About, Tattoo, Testimonial, BookingSubmission

class ArtistView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class AboutView(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

class TattooView(viewsets.ModelViewSet):
    serializer_class = TattooSerializer
    queryset = Tattoo.objects.all()

class TestimonialView(viewsets.ModelViewSet):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()

class BookingSubmissionView(viewsets.ModelViewSet):
    serializer_class = BookingSubmissionSerializer
    queryset = BookingSubmission.objects.all()
