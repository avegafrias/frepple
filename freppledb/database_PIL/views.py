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

from django.utils.translation import gettext_lazy as _

from freppledb.common.report import (
    GridReport,
    GridFieldText,
    GridFieldInteger,
    GridFieldNumber,
    GridFieldDateTime,
)

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

class ClientList(GridReport):
    title = _("clients")
    basequeryset = Client.objects.all()
    model = Client
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/client"',
            initially_hidden=True,
        ),
        GridFieldText("name", title=_("name")),
    )

class PurchaseOrderList(GridReport):
    title = _("purchase orders")
    basequeryset = PurchaseOrder.objects.all()
    model = PurchaseOrder
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/purchaseorder"',
            initially_hidden=True,
        ),
        GridFieldText(
            "client",
            title=_("client"),
            field_name="client__name",
            formatter="detail",
            extra='"role":"database_PIL/client"',
        ),
        GridFieldText("status", title=_("status")),
    )

class ProductList(GridReport):
    title = _("products")
    basequeryset = Product.objects.all()
    model = Product
    frozenColumns = 1
    rows = (
        GridFieldText(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/product"',
        ),
        GridFieldText("line", title=_("line")),
        GridFieldText("description", title=_("description")),
        GridFieldNumber("weight", title=_("weight")),
        GridFieldInteger("inventory", title=_("inventory")),
        GridFieldDateTime(
            "inventory_last_updated", title=_("inventory last updated")
        ),
    )

class OrderEntryList(GridReport):
    title = _("order entries")
    basequeryset = OrderEntry.objects.all()
    model = OrderEntry
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/orderentry"',
            initially_hidden=True,
        ),
        GridFieldInteger(
            "purchase_order",
            title=_("purchase order"),
            field_name="purchase_order_id",
            formatter="detail",
            extra='"role":"database_PIL/purchaseorder"',
        ),
        GridFieldText(
            "product",
            title=_("product"),
            field_name="product_id",
            formatter="detail",
            extra='"role":"database_PIL/product"',
        ),
        GridFieldInteger("quantity", title=_("quantity")),
    )

class OperationList(GridReport):
    title = _("operations")
    basequeryset = Operation.objects.all()
    model = Operation
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/operation"',
            initially_hidden=True,
        ),
        GridFieldText("description", title=_("description")),
    )

class ProductDependencyList(GridReport):
    title = _("product dependencies")
    basequeryset = ProductDependency.objects.all()
    model = ProductDependency
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/productdependency"',
            initially_hidden=True,
        ),
        GridFieldText(
            "product",
            title=_("product"),
            field_name="product_id",
            formatter="detail",
            extra='"role":"database_PIL/product"',
        ),
        GridFieldText(
            "operation",
            title=_("operation"),
            field_name="operation__description",
            formatter="detail",
            extra='"role":"database_PIL/operation"',
        ),
        GridFieldInteger("quantity", title=_("quantity")),
    )

class OperationDependencyList(GridReport):
    title = _("operation dependencies")
    basequeryset = OperationDependency.objects.all()
    model = OperationDependency
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/operationdependency"',
            initially_hidden=True,
        ),
        GridFieldText(
            "operation",
            title=_("operation"),
            field_name="operation__description",
            formatter="detail",
            extra='"role":"database_PIL/operation"',
        ),
        GridFieldText(
            "product",
            title=_("product"),
            field_name="product_id",
            formatter="detail",
            extra='"role":"database_PIL/product"',
        ),
        GridFieldInteger("quantity", title=_("quantity")),
    )

class ProductionFloorList(GridReport):
    title = _("production floors")
    basequeryset = ProductionFloor.objects.all()
    model = ProductionFloor
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/productionfloor"',
            initially_hidden=True,
        ),
        GridFieldText("description", title=_("description")),
    )

class ProductionSprintList(GridReport):
    title = _("production sprints")
    basequeryset = ProductionSprint.objects.all()
    model = ProductionSprint
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/productionsprint"',
            initially_hidden=True,
        ),
        GridFieldDateTime("start_date", title=_("start date")),
        GridFieldDateTime("end_date", title=_("end date")),
        GridFieldText(
            "production_floor",
            title=_("production floor"),
            field_name="production_floor__description",
            formatter="detail",
            extra='"role":"database_PIL/productionfloor"',
        ),
    )

class OperatorList(GridReport):
    title = _("operators")
    basequeryset = Operator.objects.all()
    model = Operator
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/operator"',
            initially_hidden=True,
        ),
        GridFieldText("name", title=_("name")),
    )

class ProductionStationList(GridReport):
    title = _("production stations")
    basequeryset = ProductionStation.objects.all()
    model = ProductionStation
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/productionstation"',
            initially_hidden=True,
        ),
        GridFieldText(
            "production_floor",
            title=_("production floor"),
            field_name="production_floor__description",
            formatter="detail",
            extra='"role":"database_PIL/productionfloor"',
        ),
        GridFieldText(
            "operation",
            title=_("operation"),
            field_name="operation__description",
            formatter="detail",
            extra='"role":"database_PIL/operation"',
        ),
        GridFieldText(
            "operator",
            title=_("operator"),
            field_name="operator__name",
            formatter="detail",
            extra='"role":"database_PIL/operator"',
        ),
    )

class OperatorCapacityList(GridReport):
    title = _("operator capacities")
    basequeryset = OperatorCapacity.objects.all()
    model = OperatorCapacity
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/operatorcapacity"',
            initially_hidden=True,
        ),
        GridFieldText(
            "operator",
            title=_("operator"),
            field_name="operator__name",
            formatter="detail",
            extra='"role":"database_PIL/operator"',
        ),
        GridFieldText(
            "operation",
            title=_("operation"),
            field_name="operation__description",
            formatter="detail",
            extra='"role":"database_PIL/operation"',
        ),
        GridFieldInteger("capacity", title=_("capacity")),
    )

class WorkOrderList(GridReport):
    title = _("work orders")
    basequeryset = WorkOrder.objects.all()
    model = WorkOrder
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/workorder"',
            initially_hidden=True,
        ),
        GridFieldInteger(
            "order_entry",
            title=_("order entry"),
            field_name="order_entry_id",
            formatter="detail",
            extra='"role":"database_PIL/orderentry"',
        ),
        GridFieldInteger(
            "production_station",
            title=_("production station"),
            field_name="production_station_id",
            formatter="detail",
            extra='"role":"database_PIL/productionstation"',
        ),
        GridFieldInteger("quantity", title=_("quantity")),
        GridFieldText("status", title=_("status")),
    )

class WorkOrderDependencyList(GridReport):
    title = _("work order dependencies")
    basequeryset = WorkOrderDependency.objects.all()
    model = WorkOrderDependency
    frozenColumns = 1
    rows = (
        GridFieldInteger(
            "id",
            title=_("identifier"),
            key=True,
            formatter="detail",
            extra='"role":"database_PIL/workorderdependency"',
            initially_hidden=True,
        ),
        GridFieldInteger(
            "work_order",
            title=_("work order"),
            field_name="work_order_id",
            formatter="detail",
            extra='"role":"database_PIL/workorder"',
        ),
        GridFieldInteger(
            "needed_work_order",
            title=_("needed work order"),
            field_name="needed_work_order_id",
            formatter="detail",
            extra='"role":"database_PIL/workorder"',
        ),
    )
