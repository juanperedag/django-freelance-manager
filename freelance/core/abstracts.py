from decimal import Decimal
import hashlib
from babeldjango.middleware import get_current_locale
from django.conf import settings
from django.db import models
from django.utils.translation import to_locale, get_language
from django.utils.translation import ugettext as _

try:
    from pytz import timezone
except ImportError:
    timezone = None

babel = __import__('babel', {}, {}, ['core', 'support'])
Format = babel.support.Format
Locale = babel.core.Locale

__author__ = 'fearless'


class AbstractTax(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.DecimalField(decimal_places=2, max_digits=4, default='0.00')

    class Meta:
        abstract = True


class AbstractValue(models.Model):
    """
    Abstract model for Value/Price.
    unit_value - base value
    unit_discount - percentage discount
    unit_taxes - additional percentage taxes
    unit_total - total value
    """
    unit_value = models.DecimalField(decimal_places=2, max_digits=12, default='0.00', help_text=_("The initial unit value before any discounts or taxes are applied."))
    unit_discount = models.DecimalField(decimal_places=2, max_digits=4, default='0.00', help_text=_("The discount is calculated over the initial value."))
    unit_taxes = models.ManyToManyField('freelance.Tax', help_text=_("Hold down 'Control', or 'Command' on a Mac, to select more than one."))
    unit_total = models.DecimalField(decimal_places=2, max_digits=12, default='0.00', help_text=_("The final value for a single unit."))

    class Meta:
        abstract = True

    def _get_format(self):
        locale = get_current_locale()
        if not locale:
            locale = Locale.parse(to_locale(get_language()))
        if timezone:
            tzinfo = timezone(settings.TIME_ZONE)
        else:
            tzinfo = None
        return Format(locale, tzinfo)

    def currency(self, number, currency):
        try:
            number = Decimal(number)
        except:
            number = Decimal('0.00')
        def_currency = 'USD'
        if currency:
            def_currency = currency
        return self._get_format().currency(number, def_currency)


class AbstractProduct(AbstractValue):
    """
    Abstract model for Product/Service. Inherits abstract model for User relation and abstract model for Value/Price.
    """

    title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(help_text=_("Optional description. This field is not private, it will be visible in the printable version of the document."))
    # Value
    project = models.ForeignKey('freelance.Project', null=True, blank=True, related_name='products')
    invoice = models.ForeignKey('freelance.Invoice', related_name='products')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s ( %s )" % (self.title, self.currency(self.unit_total, self.user))
