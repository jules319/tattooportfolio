from rest_framework import serializers
from .models import Artist, About, Tattoo, Testimonial, BookingSubmission

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'contact_email', 'contact_phone', 'profile_image')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'profile_image')

class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = ('id', 'artist', 'title', 'description', 'image', 'created_date')

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ('id', 'name', 'text', 'profile_image')

class BookingSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingSubmission
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number',
                   'tattoo_description', 'placement_location', 'size_inches',
                     'budget_dollars', 'reference_photos', 'submission_date')
