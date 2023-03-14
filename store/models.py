from django.db import models


# Create your models here.
class Collections(models.Model):
    title = models.CharField(max_length=255)
    # this model is going to trigger the creation of the reverse relationship in the Products class with the name "collections" which causes a clash with the already existing name. To fix this I added the related_name argument with a value of "+", which tells django not to bother creating a reverse relationship.
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name="+")

class Promotions(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    # max_length is a compulsory argument
    title = models.CharField(max_length=225)
    description = models.TextField()
    # max_digits and decimal_places are  compulsory arguments
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) 
    collections = models.ForeignKey(Collections, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotions)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHIOCES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True)
    members = models.CharField(max_length=1, choices=MEMBERSHIP_CHIOCES, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PAYMENT_STATE = [
        ("P", "Pending"),
        ("C", "Complete"),
        ("F", "Failed")
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    paymeny_status = models.CharField(max_length=1,choices=PAYMENT_STATE )
    # oneToMany relationship with the customer class
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255, default="10002")
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)