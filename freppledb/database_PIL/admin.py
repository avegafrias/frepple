#
# Copyright (C) 2026 by Partes Industriales Laguna
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from django.contrib import admin

from freppledb.admin import data_site
from freppledb.common.adminforms import MultiDBModelAdmin

from .models import (
    Client,
    OperatorCapacity,
    Operation,
    OperationDependency,
    Operator,
    OrderEntry,
    Product,
    ProductDependency,
    ProductionFloor,
    ProductionSprint,
    ProductionStation,
    PurchaseOrder,
    WorkOrder,
    WorkOrderDependency,
)


@admin.register(Client, site=data_site)
class Client_admin(MultiDBModelAdmin):
    model = Client
    save_on_top = True


@admin.register(PurchaseOrder, site=data_site)
class PurchaseOrder_admin(MultiDBModelAdmin):
    model = PurchaseOrder
    save_on_top = True


@admin.register(Product, site=data_site)
class Product_admin(MultiDBModelAdmin):
    model = Product
    save_on_top = True


@admin.register(OrderEntry, site=data_site)
class OrderEntry_admin(MultiDBModelAdmin):
    model = OrderEntry
    save_on_top = True


@admin.register(Operation, site=data_site)
class Operation_admin(MultiDBModelAdmin):
    model = Operation
    save_on_top = True


@admin.register(ProductDependency, site=data_site)
class ProductDependency_admin(MultiDBModelAdmin):
    model = ProductDependency
    save_on_top = True


@admin.register(OperationDependency, site=data_site)
class OperationDependency_admin(MultiDBModelAdmin):
    model = OperationDependency
    save_on_top = True


@admin.register(ProductionFloor, site=data_site)
class ProductionFloor_admin(MultiDBModelAdmin):
    model = ProductionFloor
    save_on_top = True


@admin.register(ProductionSprint, site=data_site)
class ProductionSprint_admin(MultiDBModelAdmin):
    model = ProductionSprint
    save_on_top = True


@admin.register(Operator, site=data_site)
class Operator_admin(MultiDBModelAdmin):
    model = Operator
    save_on_top = True


@admin.register(ProductionStation, site=data_site)
class ProductionStation_admin(MultiDBModelAdmin):
    model = ProductionStation
    save_on_top = True


@admin.register(OperatorCapacity, site=data_site)
class OperatorCapacity_admin(MultiDBModelAdmin):
    model = OperatorCapacity
    save_on_top = True


@admin.register(WorkOrder, site=data_site)
class WorkOrder_admin(MultiDBModelAdmin):
    model = WorkOrder
    save_on_top = True


@admin.register(WorkOrderDependency, site=data_site)
class WorkOrderDependency_admin(MultiDBModelAdmin):
    model = WorkOrderDependency
    save_on_top = True
