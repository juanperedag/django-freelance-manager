from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db import models

__author__ = 'fearless'


class AbstractPhoneNumber(models.Model):
    """
    Abstract model for Phone Number.
    """
    user = models.ForeignKey(User, related_name='phone_numbers')
    phone_type = models.CharField(choices=(("Home", "Home"), ("Office", "Office")), max_length=20)
    number = models.CharField(max_length=16)

    class Meta:
        abstract = True
        verbose_name = _(u"Phone number")
        verbose_name_plural = _(u"Phone numbers")

    def __unicode__(self):
        return "%s ( %s )" % (self.number, self.phone_type)


class AbstractEmailAccount(models.Model):
    """
    Abstract model for Email Account.
    """
    user = models.ForeignKey(User, related_name='email_accounts')
    email_type = models.CharField(choices=(("Home", "Home"), ("Office", "Office")), max_length=20)
    email = models.EmailField()

    class Meta:
        abstract = True
        verbose_name = _(u"Email account")
        verbose_name_plural = _(u"Email accounts")

    def __unicode__(self):
        return "%s ( %s )" % (self.email, self.email_type)


class AbstractAddress(models.Model):
    """
    Abstract model for Address.
    """
    user = models.ForeignKey(User, related_name='addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=55)
    address_type = models.CharField(choices=(("Home", "Home"), ("Office", "Office")), max_length=20)

    class Meta:
        abstract = True
        verbose_name = _(u"Address")
        verbose_name_plural = _(u"Addresses")

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.address, self.city, self.zip, self.country)


class AbstractContact(models.Model):
    """
    Abstract model for Contact.
    Each person or company you deal with, be it a client or a supplier can be referred to as a Contact in erMore.
    """
    user = models.OneToOneField(User)
    # Client
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    # Additional Info
    tax_number = models.CharField(max_length=16, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    # Phone Numbers
    # Email Accounts
    # Addresses

    class Meta:
        abstract = True
        verbose_name = _(u"Contact")
        verbose_name_plural = _(u"Contacts")

    @property
    def fullname(self):
        return self.get_fullname()

    def get_fullname(self):
        return "%s %s" % (self.firstname, self.lastname)

    def __unicode__(self):
        if self.company:
            return "%s ( %s )" % (self.get_fullname(), self.company)
        return self.get_fullname()