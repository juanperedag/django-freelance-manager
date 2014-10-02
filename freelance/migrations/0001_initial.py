# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import freelance.projects.abstracts


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=55)),
                ('state', models.CharField(max_length=55)),
                ('zip', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=55)),
                ('address_type', models.CharField(max_length=20, choices=[(b'Home', b'Home'), (b'Office', b'Office')])),
                ('user', models.ForeignKey(related_name=b'addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('tax_number', models.CharField(max_length=16, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_type', models.CharField(max_length=20, choices=[(b'Home', b'Home'), (b'Office', b'Office')])),
                ('email', models.EmailField(max_length=75)),
                ('user', models.ForeignKey(related_name=b'email_accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Email account',
                'verbose_name_plural': 'Email accounts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('date', models.DateField(help_text='The document issue date.')),
                ('notes', models.TextField(null=True, blank=True)),
                ('draft', models.BooleanField(default=True, help_text='If enabled, the document will not be taken under consideration in your balance and statistics and you will not be able to add payments. Once the document is issued (not draft) and as long as payments exist, the document status cannot be reverted.')),
                ('client_name', models.CharField(help_text='The client name, as it will appear on the document.', max_length=255)),
                ('client_address', models.CharField(max_length=255)),
                ('client_vat_number', models.CharField(max_length=16)),
                ('already_paid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(help_text="After choosing client you can have the rest fields automatically filled from the client's contact record. If the corresponding contact has many addresses, 'work' addresses will have a higher priority.", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=b'0.00', max_digits=12, decimal_places=2)),
                ('date', models.DateField()),
                ('notes', models.TextField(null=True, blank=True)),
                ('invoice', models.ForeignKey(related_name=b'payments', to='freelance.Invoice')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_type', models.CharField(max_length=20, choices=[(b'Home', b'Home'), (b'Office', b'Office')])),
                ('number', models.CharField(max_length=16)),
                ('user', models.ForeignKey(related_name=b'phone_numbers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Phone number',
                'verbose_name_plural': 'Phone numbers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_value', models.DecimalField(default=b'0.00', help_text='The initial unit value before any discounts or taxes are applied.', max_digits=12, decimal_places=2)),
                ('unit_discount', models.DecimalField(default=b'0.00', help_text='The discount is calculated over the initial value.', max_digits=4, decimal_places=2)),
                ('unit_total', models.DecimalField(default=b'0.00', help_text='The final value for a single unit.', max_digits=12, decimal_places=2)),
                ('title', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(help_text='Optional description. This field is not private, it will be visible in the printable version of the document.')),
                ('invoice', models.ForeignKey(related_name=b'products', to='freelance.Invoice')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(help_text='Optional description. This field is not private, it will be visible in the printable version of the document.')),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_goal', models.DateField(null=True, blank=True)),
                ('domain', models.CharField(max_length=50, null=True, blank=True)),
                ('sftp_host', models.CharField(max_length=50, null=True, blank=True)),
                ('sftp_password', models.CharField(max_length=50, null=True, blank=True)),
                ('sftp_username', models.CharField(max_length=50, null=True, blank=True)),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=freelance.projects.abstracts.get_upload_path)),
                ('project', models.ForeignKey(related_name=b'attachments', to='freelance.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(help_text='Optional description. This field is not private, it will be visible in the printable version of the document.')),
                ('start_date', models.DateField(null=True, blank=True)),
                ('due_goal', models.DateField(null=True, blank=True)),
                ('visible_to_client', models.BooleanField(default=False)),
                ('progress', models.DecimalField(default=b'0.00', max_digits=4, decimal_places=2)),
                ('assigned_to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='freelance.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(help_text='Optional description. This field is not private, it will be visible in the printable version of the document.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('prefix', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('percentage', models.DecimalField(default=b'0.00', max_digits=4, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(to='freelance.ProjectType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='project',
            field=models.ForeignKey(related_name=b'products', blank=True, to='freelance.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='unit_taxes',
            field=models.ManyToManyField(help_text="Hold down 'Control', or 'Command' on a Mac, to select more than one.", to='freelance.Tax'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='series',
            field=models.ForeignKey(help_text='You can optionally set a series for the document.', to='freelance.Serie'),
            preserve_default=True,
        ),
    ]
