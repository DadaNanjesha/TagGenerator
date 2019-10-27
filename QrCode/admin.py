# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Gtin
from django.db import models
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _


# Register your models here.


# noinspection PyTypeHints
class GtinAdmin(admin.ModelAdmin):
    AdminSite.app_index_title = "GTIN Associations"
    AdminSite.site_header = "QR-CODE PROJECT"
    admin.site.site_url = 'http://dada.com/'
    admin.site.site_title = 'Its Dada'
    admin.site.index_title = 'GTIN administration'
    list_display = ('gtin_number', 'product_name', 'create_date', 'update_date')
    list_filter = ('gtin_number', 'product_name')


    # class Media:


admin.site.register(Gtin, GtinAdmin)
