from django.db import models


class Company(models.Model):
    nit = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)


class Contact(models.Model):
    contact_id = models.CharField(max_length=20, primary_key=True)
    nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    last_interaction_date = models.DateField(blank=True, null=True)


class Department(models.Model):
    department_id = models.CharField(max_length=20, primary_key=True)
    department_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class ContactDepartment(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("contact_id", "department_id")


class Interaction(models.Model):
    interaction_id = models.CharField(max_length=20, primary_key=True)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    interaction_date = models.DateField(auto_now_add=True)
    interaction_type = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


class Opportunity(models.Model):
    opportunity_id = models.CharField(max_length=20, primary_key=True)
    nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(
        Contact, on_delete=models.SET_NULL, blank=True, null=True
    )
    opportunity_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    estimated_value = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    creation_date = models.DateField(auto_now_add=True)
    estimated_close_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default="open")
    success_probability = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )


class OpportunityStage(models.Model):
    stage_id = models.CharField(max_length=20, primary_key=True)
    stage_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class OpportunityStageHistory(models.Model):
    opportunity_id = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    stage_id = models.ForeignKey(OpportunityStage, on_delete=models.CASCADE)
    change_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("opportunity_id", "stage_id")


class ProductService(models.Model):
    product_service_id = models.CharField(max_length=20, primary_key=True)
    product_service_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)


class OpportunityProductService(models.Model):
    opportunity_id = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    product_service_id = models.ForeignKey(ProductService, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    negotiated_price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ("opportunity_id", "product_service_id")


class Role(models.Model):
    role_id = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class UserAccount(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)


class UserRole(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "role_id")


class Contract(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_value = models.DecimalField(max_digits=15, decimal_places=2)


class DeliveryCertificate(models.Model):
    certificate_id = models.CharField(max_length=20, primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    notes = models.TextField(blank=True, null=True)


class Category(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)


class Equipment(models.Model):
    equipment_id = models.CharField(max_length=20, primary_key=True)
    certificate_id = models.ForeignKey(DeliveryCertificate, on_delete=models.CASCADE)
    inventory_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
