from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

__author__ = 'fearless'


class AbstractSerie(models.Model):
    """
    The base serie model
    """
    title = models.CharField(max_length=255)
    prefix = models.CharField(max_length=5)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s ( %s )" % (self.prefix, self.title)


class AbstractPayment(models.Model):
    """
    The base payment model
    """

    amount = models.DecimalField(decimal_places=2, max_digits=12, default='0.00')
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    invoice = models.ForeignKey('freelance.Invoice', related_name='payments')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s ( %s )" % (self.amount, self.date)


class AbstractInvoice(models.Model):
    """
    The base invoice model. Typically an Invoices mean sales. You issue Invoices upon service or product delivery. Clients are committed to paying for your services as soon as the Invoice is issued. ErMore allows you to ease the process of online invoicing.
    """

    series = models.ForeignKey('freelance.Serie', help_text=_("You can optionally set a series for the document."))
    number = models.PositiveIntegerField()
    date = models.DateField(help_text=_("The document issue date."))
    notes = models.TextField(blank=True, null=True)
    draft = models.BooleanField(default=True, help_text=_("If enabled, the document will not be taken under consideration in your balance and statistics and you will not be able to add payments. Once the document is issued (not draft) and as long as payments exist, the document status cannot be reverted."))
    # Client
    client = models.ForeignKey(User, help_text=_("After choosing client you can have the rest fields automatically filled from the client's contact record. If the corresponding contact has many addresses, 'work' addresses will have a higher priority."))
    client_name = models.CharField(max_length=255, help_text=_("The client name, as it will appear on the document."))
    client_address = models.CharField(max_length=255)
    client_vat_number = models.CharField(max_length=16)
    # Products/Services
    # Client Already Paid
    already_paid = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s %s" % (self.series, self.number, self.client)