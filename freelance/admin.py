from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from freelance.models import EmailAccount, PhoneNumber, Address, Contact, Project, ProjectType, ProjectTask, Invoice, \
    ProjectAttachment


class EmailAccountStackedInline(admin.StackedInline):
    model = EmailAccount


class PhoneNumberStackedInline(admin.StackedInline):
    model = PhoneNumber


class AddressStackedInline(admin.StackedInline):
    model = Address


class ContactStackedInline(admin.StackedInline):
    model = Contact


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ContactStackedInline, EmailAccountStackedInline, PhoneNumberStackedInline, AddressStackedInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProjectTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectType, ProjectTypeAdmin)


class ProjectTaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectTask, ProjectTaskAdmin)


class ProjectAttachmentStackedInline(admin.StackedInline):
    model = ProjectAttachment


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectAttachmentStackedInline, )


admin.site.register(Project, ProjectAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Invoice, InvoiceAdmin)