from pathlib import Path

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
import random
from django.contrib import messages
from django.db.utils import DatabaseError
# Create your views here.

#  services = Service.objects.all()  # Fetch all services
#     return render(request, 'your_template.html', {'services': services})


# def home(request):
#     services = Service.objects.all()
#     latest_projects = Project.objects.all().order_by('-date')[:3]
#     context = {
#         'projects': latest_projects,
#     }
#     return render(request, 'index.html', context)
    # return render(request, 'index.html', {'services': services})
def fetch_records(queryset):
    try:
        return list(queryset)
    except DatabaseError:
        return []


def home(request):
    services = fetch_records(Service.objects.all())
    latest_projects = fetch_records(Project.objects.all().order_by('-date')[:3])
    context = {
        'services': services,
        'projects': latest_projects,
    }
    return render(request, 'index.html', context)


def contact_us(request):
    form = ContactForm()
    success_message = ""
    services = fetch_records(Service.objects.all())

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except DatabaseError:
                success_message = "Your message could not be saved right now."
            else:
                success_message = "Your message has been sent successfully!"
                form = ContactForm()  # Reset form after submission

    return render(request, 'contact.html', {'form': form, 'success_message': success_message, 'services': services})

def about_us(request):
    services = fetch_records(Service.objects.all())
    return render(request, 'about.html', {'services': services})


def service(request):
    services = fetch_records(Service.objects.all())
    return render(request, 'service.html', {'services': services})






# def projects(request):
#     projects = Project.objects.all().order_by('-date')  # Order by date (latest first)
#     paginator = Paginator(projects, 9)  # Show 2 projects per page
#     services = Service.objects.all()
#     page_number = request.GET.get('page')  # Get the page number from the request
#     page_obj = paginator.get_page(page_number)  # Get the correct page

#     return render(request, 'projects.html', {'page_obj': page_obj, 'services': services})
def projects(request):
    projects_list = fetch_records(Project.objects.all().order_by('-date'))
    paginator = Paginator(projects_list, 9)
    services = fetch_records(Service.objects.all())
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projects.html', {
        'page_obj': page_obj, 
        'services': services
    })

def project_detail(request, slug):
    # Get project by slug or return 404
    project = get_object_or_404(Project, slug=slug)
    
    # Get random projects excluding current one
    latest_projects = list(Project.objects.exclude(slug=slug))
    
    # Ensure we don't try to sample more than available
    sample_size = min(len(latest_projects), 3)
    if sample_size > 0:
        random_projects = random.sample(latest_projects, sample_size)
    else:
        random_projects = []
    
    return render(request, 'project_detail.html', {
        'project': project,
        'latest_projects': random_projects
    })

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')



# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     latest_projects = list(Project.objects.exclude(id=project_id))  # Convert queryset to list
#     random_projects = random.sample(latest_projects, min(len(latest_projects), 3))  # Pick 3 random projects
    
#     return render(request, 'project_detail.html', {
#         'project': project,
#         'latest_projects': random_projects
#     })



# def service_detail(request, service_id):
#     service = get_object_or_404(Service, id=service_id)
#     services = Service.objects.all()
#     services_random = list(Service.objects.all())
#     random.shuffle(services_random)
#     return render(request, 'service_detail.html', {'service': service, 'services': services,'services_random': services_random })

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all()
    services_random = list(Service.objects.exclude(slug=slug))
    random.shuffle(services_random)
    return render(request, 'service_detail.html', {
        'service': service, 
        'services': services,
        'services_random': services_random[:3]  # Limit to 3 random services
    })

# New SEO-friendly view
def seo_service_detail(request, country_slug, service_slug):
    # Get country from slug
    country = get_object_or_404(Country, slug=country_slug)
    
    # Get service with both slug and country match
    service = get_object_or_404(
        Service,
        slug=service_slug,  # Assuming you use slugs for services
        countries=country
    )
    
    services = Service.objects.all()
    services_random = list(services)
    random.shuffle(services_random)
    
    return render(request, 'service_detail.html', {
        'service': service,
        'country': country,
        'services': services,
        'services_random': services_random
    })


def seo_project_detail(request, slug):
    # Retrieve the project by its slug or return 404 if not found
    project = get_object_or_404(Project, slug=slug)
    
    return render(request, 'project_detail.html', {
        'project': project,
    })



def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service
            booking.save()
            
            messages.success(request, "Your booking was successful! You will be redirected shortly.")
            return redirect('booking_success', service_id=service.id)  # Redirect to success page

    return redirect('service_detail', service_id=service.id)  # If form is invalid, go back

def booking_success(request, service_id):
    return render(request, 'booking_success.html', {'service_id': service_id})


# views.py
def diving_company_lagos(request):
    return render(request, 'diving-company-lagos.html')

def diving_company_abidjan(request):
    return render(request, 'diving-company-abidjan.html')

def diving_company_cotonou(request):
    return render(request, 'diving-company-cotonou.html')

def diving_company_lome(request):
    return render(request, 'diving-company-lome.html')

def diving_company_conakry(request):
    return render(request, 'diving-company-conakry.html')

def diving_company_senegal(request):
    return render(request, 'diving-company-senegal.html')

# Underwater Company Views
def underwater_company_lagos(request):
    return render(request, 'underwater-company-lagos.html')

def underwater_company_abidjan(request):
    return render(request, 'underwater-company-abidjan.html')

def underwater_company_cotonou(request):
    return render(request, 'underwater-company-cotonou.html')

def underwater_company_lome(request):
    return render(request, 'underwater-company-lome.html')

def underwater_company_conakry(request):
    return render(request, 'underwater-company-conakry.html')

def underwater_company_senegal(request):
    return render(request, 'underwater-company-senegal.html')

# Marine Company Views
def marine_company_abidjan(request):
    return render(request, 'marine-company-abidjan.html')

def marine_company_cotonou(request):
    return render(request, 'marine-company-cotonou.html')

def marine_company_lome(request):
    return render(request, 'marine-company-lome.html')

def marine_company_conakry(request):
    return render(request, 'marine-company-conakry.html')

def marine_company_senegal(request):
    return render(request, 'marine-company-senegal.html')
def marine_company_lagos(request):
    return render(request, 'marine-company-lagos.html')

# In-Water Inspection Views
def inwater_inspection_lagos(request):
    return render(request, 'inwater-inspection-lagos.html')

def inwater_inspection_abidjan(request):
    return render(request, 'inwater-inspection-abidjan.html')

def inwater_inspection_cotonou(request):
    return render(request, 'inwater-inspection-cotonou.html')

def inwater_inspection_lome(request):
    return render(request, 'inwater-inspection-lome.html')

def inwater_inspection_conakry(request):
    return render(request, 'inwater-inspection-conakry.html')

def inwater_inspection_senegal(request):
    return render(request, 'inwater-inspection-senegal.html')

#this is for SEO
def robots_txt(request):
    return render(request, 'robots.txt', content_type="text/plain")

def llms_txt(request):
    file_path = Path(settings.BASE_DIR) / "llms.txt"
    return FileResponse(file_path.open("rb"), content_type="text/plain; charset=utf-8")
