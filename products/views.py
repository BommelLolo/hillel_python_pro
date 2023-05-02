import csv
import weasyprint

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, ListView
from django.urls import reverse_lazy


from products.forms import ImportCSVForm
from products.models import Product


class ProductView(ListView):
    context_object_name = 'products'
    template_name = 'products/index.html'
    model = Product


def export_csv(request, *args, **kwargs):
    headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="VolleyMAG-products.csv"'
    }
    response = HttpResponse(headers=headers)
    fields_name = ['name', 'description', 'sku', 'image', 'price', 'is_active']
    writer = csv.DictWriter(response, fieldnames=fields_name)
    writer.writeheader()
    for product in Product.objects.iterator():
        writer.writerow(
            {
                'name': product.name,
                'description': product.description,
                'sku': product.sku,
                'image': product.image.name if product.image else 'no image',
                'price': product.price,
                'is_active': product.is_active
            }
        )
    return response


class ExportToPdf(TemplateView):
    template_name = 'products/pdf.html'

    def get(self, request, *args, **kwargs):
        context = {'products': Product.objects.all()}
        headers = {
            'Content-Type': 'application/pdf',
            'Content-Disposition': 'attachment; filename="products.pdf"'
        }
        html = render_to_string(
            template_name=self.template_name,
            context=context
        )
        pdf = weasyprint.HTML(string=html).write_pdf()
        response = HttpResponse(pdf, headers=headers)
        return response


class ImportCSV(FormView):
    form_class = ImportCSVForm
    template_name = 'products/import_csv.html'
    success_url = reverse_lazy('products')

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
