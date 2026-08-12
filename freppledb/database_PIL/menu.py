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

import freppledb.database_PIL.views
from freppledb.menu import menu

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

menu.addItem(
    "inventory",
    "clients",
    url="/data/database_PIL/client/",
    report=freppledb.database_PIL.views.ClientList,
    index=1400,
    model=Client,
)
menu.addItem(
    "inventory",
    "purchase orders",
    url="/data/database_PIL/purchaseorder/",
    report=freppledb.database_PIL.views.PurchaseOrderList,
    index=1410,
    model=PurchaseOrder,
    dependencies=[Client],
)
menu.addItem(
    "inventory",
    "products",
    url="/data/database_PIL/product/",
    report=freppledb.database_PIL.views.ProductList,
    index=1420,
    model=Product,
)
menu.addItem(
    "inventory",
    "order entries",
    url="/data/database_PIL/orderentry/",
    report=freppledb.database_PIL.views.OrderEntryList,
    index=1430,
    model=OrderEntry,
    dependencies=[PurchaseOrder, Product],
)
menu.addItem(
    "inventory",
    "PIL operations",
    url="/data/database_PIL/operation/",
    report=freppledb.database_PIL.views.OperationList,
    index=1440,
    model=Operation,
)
menu.addItem(
    "inventory",
    "product dependencies",
    url="/data/database_PIL/productdependency/",
    report=freppledb.database_PIL.views.ProductDependencyList,
    index=1450,
    model=ProductDependency,
    dependencies=[Product, Operation],
)
menu.addItem(
    "inventory",
    "operation dependencies",
    url="/data/database_PIL/operationdependency/",
    report=freppledb.database_PIL.views.OperationDependencyList,
    index=1460,
    model=OperationDependency,
    dependencies=[Operation, Product],
)
menu.addItem(
    "inventory",
    "production floors",
    url="/data/database_PIL/productionfloor/",
    report=freppledb.database_PIL.views.ProductionFloorList,
    index=1470,
    model=ProductionFloor,
)
menu.addItem(
    "inventory",
    "production sprints",
    url="/data/database_PIL/productionsprint/",
    report=freppledb.database_PIL.views.ProductionSprintList,
    index=1480,
    model=ProductionSprint,
    dependencies=[ProductionFloor],
)
menu.addItem(
    "inventory",
    "operators",
    url="/data/database_PIL/operator/",
    report=freppledb.database_PIL.views.OperatorList,
    index=1490,
    model=Operator,
)
menu.addItem(
    "inventory",
    "production stations",
    url="/data/database_PIL/productionstation/",
    report=freppledb.database_PIL.views.ProductionStationList,
    index=1500,
    model=ProductionStation,
    dependencies=[ProductionFloor, Operation, Operator],
)
menu.addItem(
    "inventory",
    "operator capacities",
    url="/data/database_PIL/operatorcapacity/",
    report=freppledb.database_PIL.views.OperatorCapacityList,
    index=1510,
    model=OperatorCapacity,
    dependencies=[Operator, Operation],
)
menu.addItem(
    "inventory",
    "work orders",
    url="/data/database_PIL/workorder/",
    report=freppledb.database_PIL.views.WorkOrderList,
    index=1520,
    model=WorkOrder,
    dependencies=[ProductionStation, OrderEntry],
)
menu.addItem(
    "inventory",
    "work order dependencies",
    url="/data/database_PIL/workorderdependency/",
    report=freppledb.database_PIL.views.WorkOrderDependencyList,
    index=1530,
    model=WorkOrderDependency,
    dependencies=[WorkOrder],
)

# this code runs after the items are added to the Inventory dropdown
for name in (
    "inventory detail",
    "distribution orders",
    "buffer admin",
    "item distributions",
    "distribution order summary",
    "inventory report",
    "problem report",
):
    menu.removeItem("inventory", name)
