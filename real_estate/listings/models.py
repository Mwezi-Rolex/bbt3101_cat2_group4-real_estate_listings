from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message="Enter a valid phone number.")]
    )
    agency = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.agency})"


class PropertyType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Property Type"
        verbose_name_plural = "Property Types"

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    location = models.CharField(max_length=200)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name="properties")
    size_sqft = models.FloatField(validators=[MinValueValidator(0)])
    date_listed = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="properties")

    class Meta:
        ordering = ['-date_listed']

    def __str__(self):
        return f"{self.title} - {self.location}"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="property_images/")
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.property.title}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message="Enter a valid phone number.")]
    )

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="bookings")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    class Meta:
        unique_together = ('client', 'property')
        ordering = ['-date_sent']

    def __str__(self):
        return f"Booking by {self.client.name} for {self.property.title} ({self.status})"
