from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout,authenticate
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy
from .models import CustomUser, UserProfile, Military
from .forms import LoginForm, ProfileForm, MilitaryRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from ordering.models import Order
from django.db.models import Q

from django.db import transaction

def registration(request):
    if request.method == 'POST':
        form = MilitaryRegistrationForm(request.POST)
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            military_unit = form.cleaned_data['military_unit']
            military_rank = form.cleaned_data['military_rank']
            
            # Use atomic transaction to ensure data consistency
            with transaction.atomic():
                # Create a new user account
                user = CustomUser.objects.create_user(username=username, password=password, email=email, \
                    first_name=first_name, last_name=last_name)
                
                # Create a Military instance and associate it with the user
                military = Military.objects.create(user=user, military_unit=military_unit, military_rank=military_rank)

            login(request, user)

            return redirect('profile')
    else:
        form = MilitaryRegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})




class CustomLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('dashboard')
            else:
                error = 'Invalid login credentials.'
        else:
            error = 'Invalid form data.'

        return render(request, 'registration/login.html', {'form': form, 'error': error})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    user = request.user
    military = None
    volunteer = None
    deliveryman = None

    if hasattr(user, 'military'):
        military = user.military
    elif hasattr(user, 'volunteer'):
        volunteer = user.volunteer
    elif hasattr(user, 'deliveryman'):
        deliveryman = user.deliveryman

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user

            if military:
                profile.military_military_unit = military.military_unit
                profile.military_military_rank = military.military_rank
            elif deliveryman:
                profile.deliveryman_status = deliveryman.status

            profile.save()
            return redirect('profile')

    else:
        initial = {}
        if military:
            initial.update({
                'military_military_unit': military.military_unit,
                'military_military_rank': military.military_rank,
            })
        elif deliveryman:
            initial.update({
                'deliveryman_status': deliveryman.status,
            })

        form = ProfileForm(instance=user, initial=initial)

    context = {'user': user, 'form': form}
    return render(request, 'profile.html', context)


@login_required
def dashboard(request):
    user = request.user
    orders = Order.objects.filter(military=user)
    deliverymans = Order.objects.filter(deliveryman=user)
    incoming_orders = Order.objects.filter(status="is_expected").count()

    count = {
        'not_confirmed': orders.filter(status='not_confirmed').count(),
        'confirmed': orders.filter(status='confirmed').count(),
        'in_transit': orders.filter(status='in_transit').count(),
        'delivered': orders.filter(status='delivered').count(),
        'canceled': orders.filter(status='canceled').count(),
        'is_expected': orders.filter(status="is_expected").count(),

        'tasks' : deliverymans.filter(status="confirmed", deliveryman=user).count(),
        'delivered' : deliverymans.filter(status="delivered", deliveryman=user).count(),
        'in_transit_delivery' : deliverymans.filter(status="in_transit", deliveryman=user).count(),
    }
    context = {
        'count': count,
        'user': user,
        'deliverymans' : deliverymans,
        'orders' : orders,
        'incoming_orders': incoming_orders,
    }
    return render(request, 'dashboard.html', context)