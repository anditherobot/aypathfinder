from django.db import models

# Create your models here.


class RegistrantInfo(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    phone_number = models.CharField(max_length=50, verbose_name="Phone #")
    email = models.EmailField(max_length=100, verbose_name="Email")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    grade = models.CharField(max_length=100)
    church = models.CharField(max_length=100)

    #
    iwaspathfinder = models.BooleanField(default=False, verbose_name="I have been a Pathfinder")
    ifyespathfinder = models.CharField(max_length=100, verbose_name="at (Enter Previous Pathfinder Club Name)", blank=True, null=True)
    dadismasterguide = models.BooleanField(default=False, verbose_name="My dad is a Master Guide")
    dadwaspathfinder = models.BooleanField(default=False, verbose_name="My father has been a Pathfinder")
    momismasterguide = models.BooleanField(default=False, verbose_name="My mother is a Master Guide")
    momwaspathfinder = models.BooleanField(default=False, verbose_name="My mother has been a Pathfinder")
    
    wishspecialclub = models.CharField(max_length=100, verbose_name="I wish to join the following Special Club Program",blank=True, null=True)

    def __str__(self):
        return "first Name" + self.first_name


class RegistrationCheckList(models.Model):
    registrant = models.ForeignKey(RegistrantInfo, on_delete = models.CASCADE, editable= False, null=True, blank=True)
    #get name here
    registration_completed = models.BooleanField(default=False, verbose_name="Registration/ Re-Enrollment form completed and signed")
    health_completed = models.BooleanField(default=False, verbose_name="Health form completed and signed")
    registration_fee = models.BooleanField(default=False, verbose_name="Registration/ Re-Enrollment fee")
    registration_fee_amount = models.IntegerField(default=0, verbose_name="Registration Fee Amount")
    prior_fees = models.BooleanField(default=False, verbose_name="Prior year unpaid club dues")
    prior_fees_amount = models.IntegerField(default=0, verbose_name="Prior year Fee Amount")
    atlantic_fees = models.BooleanField(default=False, verbose_name="Atlantic Union Camporee fee (with form)")
    atlantic_fees_amount = models.IntegerField(default=0, verbose_name="Atlantic Union Camporee fee Amount")
    bayda_fees = models.BooleanField(default=False, verbose_name="BAYDA Youth congress fee/deposit")
    bayda_fees_amount = models.IntegerField(default=0, verbose_name="BAYDA Youth congress fee/deposit Amount")
    other_fees = models.BooleanField(default=False, verbose_name="Other")
    other_fees_amount = models.IntegerField(default=0, verbose_name="Other Amount")
    
    class_assigned = models.CharField(max_length=50,  blank=True, verbose_name="Assigned to class.")
    unit_assigned = models.CharField(max_length=50,  blank=True, verbose_name="Placed in unit.")

    package_workbook = models.BooleanField(default=False, verbose_name="Class workbook (welcome letter, code of conduct, points policy, Uniform FAQ, current year program schedule)")
    package_pathfindertshirt = models.BooleanField(default=False, verbose_name="Pathfinder t-shirt(to new Pathfinder only, if not given in prior year)")

    package_sweatshirt = models.BooleanField(default=False, verbose_name="Pathfinder sweat shirt(to new Pathfinder only, if not given in prior year)")
    package_adventurertshirt = models.BooleanField(default=False, verbose_name="Adventurer t-shirt (to new Pathfinder only, if not given in prior year)")
   
    package_namebadge = models.CharField(max_length=100,  blank=True, verbose_name="Name badge for")
    date_updated = models.DateField(null=True, blank=True, verbose_name="Date Updated")

   



