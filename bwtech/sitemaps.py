# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
# from .models import Service, Project
# from django.utils.text import slugify

# class StaticViewSitemap(Sitemap):
#     changefreq = 'monthly'
#     priority = 0.8

#     def items(self):
#         return ['home', 'about-us', 'contact-us',  'projects']

#     def location(self, item):
#         return reverse(item)



# class ServiceSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

#     def items(self):
#         # Generate a list of (service, country) tuples
#         services = Service.objects.prefetch_related('countries').all()
#         items = []
#         for service in services:
#             for country in service.countries.all():
#                 items.append((service, country))
#         return items

#     def location(self, item):
#         service, country = item
#         service_slug = slugify(service.title)
#         country_slug = country.get_slug()
#         return f"/services/{country_slug}/{service_slug}/"


# class ProjectSitemap(Sitemap):
#     changefreq = 'monthly'
#     priority = 0.7

#     def items(self):
#         return Project.objects.all()

#     def location(self, obj):
#         return f"/projects/{obj.name}/"



from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service, Project

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['home', 'about-us', 'contact-us', 'services', 'projects', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)

class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # All 24 location-based service pages
        locations = ['lagos', 'abidjan', 'cotonou', 'lome', 'conakry', 'senegal']
        service_types = [
            'diving-company',
            'underwater-inspections-company', 
            'marine-company',
            'in-water-inspection'
        ]
        
        items = []
        for service_type in service_types:
            for location in locations:
                items.append(f"{service_type}/{location}")
        return items

    def location(self, item):
        return f"/service/{item}/"

class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse('project_detail', kwargs={'slug': obj.slug})

class ServiceDetailSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return reverse('service_detail', kwargs={'slug': obj.slug})

class SEOServiceDetailSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # Generate items for seo_service_detail URLs
        # You might need to adjust this based on your model structure
        services = Service.objects.prefetch_related('countries').all()
        items = []
        for service in services:
            for country in service.countries.all():
                items.append({
                    'service_slug': service.slug,
                    'country_slug': country.slug  # adjust based on your country model
                })
        return items

    def location(self, obj):
        return f"/services/{obj['country_slug']}/{obj['service_slug']}/"

class BookServiceSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return reverse('book_service', kwargs={'service_id': obj.id})

class BookingSuccessSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return reverse('booking_success', kwargs={'service_id': obj.id})

# Update your sitemaps dictionary to include all
sitemaps = {
    'services': ServiceSitemap,  # 24 location pages
    'projects': ProjectSitemap,
    'static': StaticViewSitemap,
    'service_details': ServiceDetailSitemap,  # dynamic service pages
    'seo_service_details': SEOServiceDetailSitemap,  # country/service pages
    'book_services': BookServiceSitemap,
    'booking_success': BookingSuccessSitemap,
}