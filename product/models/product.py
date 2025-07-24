#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models

from product.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    # category = models.ManyToManyField(Category, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    def __str__(self):
        return self.title
