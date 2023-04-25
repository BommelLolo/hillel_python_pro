from django.urls import path

from products.views import ProductView, export_csv, ExportToPdf, ImportCSV

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('export-csv/', export_csv, name='products_to_csv'),
    path('export-pdf/', ExportToPdf.as_view(), name='products_to_pdf'),
    path('import-csv/', ImportCSV.as_view(), name='products_from_csv'),
]
