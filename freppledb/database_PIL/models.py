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

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "client_pil"

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "purchase_order_pil"

    def __str__(self):
        return f"PO #{self.pk}"

class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    line = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    inventory_last_updated = models.DateTimeField()

    class Meta:
        db_table = "product_pil"

    def __str__(self):
        return self.id

class OrderEntry(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "order_entry_pil"

    def __str__(self):
        return f"{self.product_id} x{self.quantity}"

class Operation(models.Model):
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "operation_pil"

    def __str__(self):
        return self.description

class ProductDependency(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "product_dependency_pil"

    def __str__(self):
        return f"{self.product_id} <- {self.operation_id}"

class OperationDependency(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "operation_dependency_pil"

    def __str__(self):
        return f"{self.operation_id} <- {self.product_id}"

class ProductionFloor(models.Model):
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "production_floor_pil"

    def __str__(self):
        return self.description

class ProductionSprint(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    production_floor = models.ForeignKey(ProductionFloor, on_delete=models.CASCADE)

    class Meta:
        db_table = "production_sprint_pil"
        unique_together = (("start_date", "end_date", "production_floor"),)

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"

class Operator(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "operator_pil"

    def __str__(self):
        return self.name

class ProductionStation(models.Model):
    production_floor = models.ForeignKey(ProductionFloor, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    class Meta:
        db_table = "production_station_pil"

    def __str__(self):
        return f"Station #{self.pk}"

class OperatorCapacity(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    class Meta:
        db_table = "operator_capacity_pil"

    def __str__(self):
        return f"{self.operator_id} @ {self.operation_id}: {self.capacity}"

class WorkOrder(models.Model):
    order_entry = models.ForeignKey(OrderEntry, on_delete=models.CASCADE)
    production_station = models.ForeignKey(ProductionStation, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "work_order_pil"

    def __str__(self):
        return f"WO #{self.pk}"

class WorkOrderDependency(models.Model):
    work_order = models.ForeignKey(
        WorkOrder, on_delete=models.CASCADE, related_name="dependencies"
    )
    needed_work_order = models.ForeignKey(
        WorkOrder, on_delete=models.CASCADE, related_name="needed_by"
    )

    class Meta:
        db_table = "work_order_dependency_pil"

    def __str__(self):
        return f"{self.work_order_id} needs {self.needed_work_order_id}"
