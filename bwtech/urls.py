from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import ServiceSitemap, ProjectSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps  

# sitemaps = {
#     'services': ServiceSitemap,
#     'projects': ProjectSitemap,
#     'static': StaticViewSitemap,  # Added static pages
# }

urlpatterns = [
    #site maps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('llms.txt', llms_txt, name='llms_txt'),
    path('bwtech2026indexnowkey9876543210ab.txt', indexnow_key, name='indexnow_key'),
    path('services/<str:country_slug>/<str:service_slug>/', seo_service_detail, name='seo_service_detail'),   
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('projects/<slug:slug>/', seo_project_detail, name='seo_project_detail'),



     path('service/diving-company/lagos/', diving_company_lagos, name='diving_company_lagos'),
    path('service/diving-company/abidjan/', diving_company_abidjan, name='diving_company_abidjan'),
    path('service/diving-company/cotonou/', diving_company_cotonou, name='diving_company_cotonou'),
    path('service/diving-company/lome/', diving_company_lome, name='diving_company_lome'),
    path('service/diving-company/conakry/', diving_company_conakry, name='diving_company_conakry'),
    path('service/diving-company/senegal/', diving_company_senegal, name='diving_company_senegal'),
    
    # Underwater Company URLs
    path('service/underwater-survey-company/lagos/', underwater_company_lagos, name='underwater_company_lagos'),
    path('service/underwater-survey-company/abidjan/', underwater_company_abidjan, name='underwater_company_abidjan'),
    path('service/underwater-survey-company/cotonou/', underwater_company_cotonou, name='underwater_company_cotonou'),
    path('service/underwater-survey-company/lome/', underwater_company_lome, name='underwater_company_lome'),
    path('service/underwater-survey-company/conakry/', underwater_company_conakry, name='underwater_company_conakry'),
    path('service/underwater-survey-company/senegal/', underwater_company_senegal, name='underwater_company_senegal'),
    
    # Marine Company URLs
    path('service/marine-company/lagos/', marine_company_lagos, name='marine_company_lagos'),
    path('service/marine-company/abidjan/', marine_company_abidjan, name='marine_company_abidjan'),
    path('service/marine-company/cotonou/', marine_company_cotonou, name='marine_company_cotonou'),
    path('service/marine-company/lome/', marine_company_lome, name='marine_company_lome'),
    path('service/marine-company/conakry/', marine_company_conakry, name='marine_company_conakry'),
    path('service/marine-company/senegal/', marine_company_senegal, name='marine_company_senegal'),
    
    # In-Water Inspection URLs
    path('service/underwater-inspections/lagos/', inwater_inspection_lagos, name='inwater_inspection_lagos'),
    path('service/underwater-inspections/abidjan/', inwater_inspection_abidjan, name='inwater_inspection_abidjan'),
    path('service/underwater-inspections/cotonou/', inwater_inspection_cotonou, name='inwater_inspection_cotonou'),
    path('service/underwater-inspections/lome/', inwater_inspection_lome, name='inwater_inspection_lome'),
    path('service/underwater-inspections/conakry/', inwater_inspection_conakry, name='inwater_inspection_conakry'),
    path('service/underwater-inspections/senegal/', inwater_inspection_senegal, name='inwater_inspection_senegal'),


    # Static pages (added to sitemap)
    path('', home, name="home"),
    path('contact-us/', contact_us, name="contact-us"),
    path('about-us/', about_us, name="about-us"),
    path('services/', service, name="services"),
    path('projects/', projects, name="projects"),
    path('privacy-policy/', privacy, name='privacy'),
    path('terms-and-conditions/', terms, name='terms'),

    # Dynamic pages
    # path('projects/<int:project_id>/', project_detail, name='project_detail'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
    # path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('services/<slug:slug>/', service_detail, name='service_detail'),    
    path('book/<int:service_id>/', book_service, name='book_service'),

    path('booking-success/<int:service_id>/', booking_success, name='booking_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
