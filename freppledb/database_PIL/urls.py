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

from django.urls import re_path

from freppledb import mode

# Automatically add these URLs when the application is installed
autodiscover = True

if mode == "WSGI":
    from . import views

    urlpatterns = [
        re_path(
            r"^data/database_PIL/client/$",
            views.ClientList.as_view(),
            name="database_PIL_client_changelist",
        ),
        re_path(
            r"^data/database_PIL/purchaseorder/$",
            views.PurchaseOrderList.as_view(),
            name="database_PIL_purchaseorder_changelist",
        ),
        re_path(
            r"^data/database_PIL/product/$",
            views.ProductList.as_view(),
            name="database_PIL_product_changelist",
        ),
        re_path(
            r"^data/database_PIL/orderentry/$",
            views.OrderEntryList.as_view(),
            name="database_PIL_orderentry_changelist",
        ),
        re_path(
            r"^data/database_PIL/operation/$",
            views.OperationList.as_view(),
            name="database_PIL_operation_changelist",
        ),
        re_path(
            r"^data/database_PIL/productdependency/$",
            views.ProductDependencyList.as_view(),
            name="database_PIL_productdependency_changelist",
        ),
        re_path(
            r"^data/database_PIL/operationdependency/$",
            views.OperationDependencyList.as_view(),
            name="database_PIL_operationdependency_changelist",
        ),
        re_path(
            r"^data/database_PIL/productionfloor/$",
            views.ProductionFloorList.as_view(),
            name="database_PIL_productionfloor_changelist",
        ),
        re_path(
            r"^data/database_PIL/productionsprint/$",
            views.ProductionSprintList.as_view(),
            name="database_PIL_productionsprint_changelist",
        ),
        re_path(
            r"^data/database_PIL/operator/$",
            views.OperatorList.as_view(),
            name="database_PIL_operator_changelist",
        ),
        re_path(
            r"^data/database_PIL/productionstation/$",
            views.ProductionStationList.as_view(),
            name="database_PIL_productionstation_changelist",
        ),
        re_path(
            r"^data/database_PIL/operatorcapacity/$",
            views.OperatorCapacityList.as_view(),
            name="database_PIL_operatorcapacity_changelist",
        ),
        re_path(
            r"^data/database_PIL/workorder/$",
            views.WorkOrderList.as_view(),
            name="database_PIL_workorder_changelist",
        ),
        re_path(
            r"^data/database_PIL/workorderdependency/$",
            views.WorkOrderDependencyList.as_view(),
            name="database_PIL_workorderdependency_changelist",
        ),
    ]
