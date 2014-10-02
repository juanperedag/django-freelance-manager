from freelance.contacts.abstracts import AbstractPhoneNumber, AbstractEmailAccount, AbstractAddress, AbstractContact
from freelance.core.abstracts import AbstractProduct, AbstractTax
from freelance.invoicing.abstracts import AbstractPayment, AbstractSerie, AbstractInvoice
from freelance.projects.abstracts import AbstractType, AbstractTask, AbstractProject, AbstractAttachment


class PhoneNumber(AbstractPhoneNumber):
    pass


class EmailAccount(AbstractEmailAccount):
    pass


class Address(AbstractAddress):
    pass


class Contact(AbstractContact):
    pass


class Payment(AbstractPayment):
    pass


class Serie(AbstractSerie):
    pass


class Invoice(AbstractInvoice):
    pass


class Product(AbstractProduct):
    pass


class Tax(AbstractTax):
    pass


class ProjectAttachment(AbstractAttachment):
    pass


class ProjectType(AbstractType):
    pass


class ProjectTask(AbstractTask):
    pass


class Project(AbstractProject):
    pass
