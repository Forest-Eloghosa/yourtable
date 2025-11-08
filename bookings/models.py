from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('menu.Restaurant', on_delete=models.CASCADE)
    date = models.DateTimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking for {self.guests} at {self.restaurant} on {self.date}"


class BookingImage(models.Model):
    booking = models.ForeignKey(Booking, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for booking {self.booking.id}"
    

class Table(models.Model):
    restaurant = models.ForeignKey('menu.Restaurant', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('restaurant', 'number')

    def __str__(self):
        return f"Table {self.number} at {self.restaurant} (Capacity: {self.capacity})"


class Reservation(models.Model):
    booking = models.ForeignKey(Booking, related_name='reservations', on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation of {self.table} for booking {self.booking.id}"


class Payment(models.Model):
    booking = models.OneToOneField(Booking, related_name='payment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Payment of {self.amount} for booking {self.booking.id}"


class BookingStatus(models.Model):
    booking = models.OneToOneField(Booking, related_name='status', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Status of booking {self.booking.id}: {self.status}"


class Feedback(models.Model):
    booking = models.OneToOneField(Booking, related_name='feedback', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for booking {self.booking.id}: {self.rating} stars"


class CancellationPolicy(models.Model):
    restaurant = models.ForeignKey('menu.Restaurant', on_delete=models.CASCADE)
    policy_text = models.TextField()

    def __str__(self):
        return f"Cancellation Policy for {self.restaurant}"


class Cancellation(models.Model):
    booking = models.OneToOneField(Booking, related_name='cancellation', on_delete=models.CASCADE)
    reason = models.TextField()
    canceled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancellation of booking {self.booking.id}"


class SpecialOffer(models.Model):
    restaurant = models.ForeignKey('menu.Restaurant', on_delete=models.CASCADE)
    description = models.TextField()
    discount_percentage = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Special Offer at {self.restaurant}: {self.discount_percentage}% off"
    
