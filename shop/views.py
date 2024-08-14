from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import F
from django.views import View
from .models import Brand, Mobile
from .forms import CreateBrandForm, CreateMobileForm


class AddBrandView(View):
    form_class = CreateBrandForm
    template_name = 'phone/add_brand.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateBrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
        return render(request, self.template_name, {'form': form})


class AddMobileView(View):
    form_class = CreateMobileForm
    template_name = 'phone/add_phone.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateMobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
        return render(request, self.template_name, {'form': form})


class MobileListView(View):

    def get(self, request):
        brands = Brand.objects.filter(nationality='Korea')
        mobiles = Mobile.objects.all()

        if 'brand_name' in request.GET:
            brand_name = request.GET.get('brand_name')
            mobiles = mobiles.filter(brand__name=brand_name)

        mobiles_same_nationality = Mobile.objects.filter(brand__nationality=F('manufacture_country'))

        context = {
            'brands': brands,
            'mobiles': mobiles,
            'mobiles_same_nationality': mobiles_same_nationality
        }
        return render(request, 'phone/phone_list.html', context)


class MobilesKoreanBrandView(View):
    def get(self, request):
        mobiles = Mobile.objects.filter(brand__nationality='Korea')
        return render(request, 'filter/korea.html', {'mobiles': mobiles})


class MobilesWithMatchingNationalityView(View):
    def get(self, request):
        mobiles = Mobile.objects.filter(brand__nationality=F('manufacture_country'))
        return render(request, 'filter/same.html', {'mobiles': mobiles})
