from rest_framework import serializers
from .models import Agent, Property, PropertyImage, Client, Booking, PropertyType


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    agent = AgentSerializer(read_only=True)  # show agent details, not just ID
    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.all(), source="agent", write_only=True
    )
    property_type = PropertyTypeSerializer(read_only=True)
    property_type_id = serializers.PrimaryKeyRelatedField(
        queryset=PropertyType.objects.all(), source="property_type", write_only=True
    )

    class Meta:
        model = Property
        fields = [
            "id", "title", "description", "price", "location", 
            "size_sqft", "date_listed", 
            "property_type", "property_type_id", 
            "agent", "agent_id", 
            "images"
        ]
        read_only_fields = ["date_listed"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_size_sqft(self, value):
        if value <= 0:
            raise serializers.ValidationError("Size must be greater than zero.")
        return value


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source="client", write_only=True
    )
    property = PropertySerializer(read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all(), source="property", write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            "id", "client", "client_id", "property", "property_id",
            "message", "date_sent", "status"
        ]
        read_only_fields = ["date_sent"]

    def validate(self, data):
        """ Prevent duplicate active bookings for the same property by same client """
        client = data.get("client")
        property = data.get("property")

        if Booking.objects.filter(client=client, property=property).exists():
            raise serializers.ValidationError("This client already has a booking for this property.")

        return data
