from django.contrib import admin

from .models import (
    Category,
    Company,
    Contact,
    ContactDepartment,
    Contract,
    DeliveryCertificate,
    Department,
    Equipment,
    Interaction,
    Opportunity,
    OpportunityProductService,
    OpportunityStage,
    OpportunityStageHistory,
    ProductService,
    Role,
    UserAccount,
    UserRole,
)


class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]


class ContactDepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactDepartment._meta.fields]


class InteractionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Interaction._meta.fields]


class OpportunityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Opportunity._meta.fields]


class OpportunityStageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OpportunityStage._meta.fields]


class OpportunityStageHistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OpportunityStageHistory._meta.fields]


class ProductServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductService._meta.fields]


class OpportunityProductServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OpportunityProductService._meta.fields]


class RoleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Role._meta.fields]


class UserAccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserAccount._meta.fields]


class UserRoleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserRole._meta.fields]


class ContractAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contract._meta.fields]


class DeliveryCertificateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeliveryCertificate._meta.fields]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.fields]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ContactDepartment, ContactDepartmentAdmin)
admin.site.register(Interaction, InteractionAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(OpportunityStage, OpportunityStageAdmin)
admin.site.register(OpportunityStageHistory, OpportunityStageHistoryAdmin)
admin.site.register(ProductService, ProductServiceAdmin)
admin.site.register(OpportunityProductService, OpportunityProductServiceAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(DeliveryCertificate, DeliveryCertificateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
