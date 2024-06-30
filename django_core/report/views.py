from django.shortcuts import render, redirect
from django.contrib import messages
from django_module_basic.models import Area, ModelTest, User,Report
from .forms import CheckInForm, CheckOutForm
from datetime import datetime
from django.utils import timezone

def check_in(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data.get('area')
            code = form.cleaned_data.get('code')
            class_model = form.cleaned_data.get('class_model')
            try:
                model_instance = ModelTest.objects.get(code=code)
                first_name = model_instance.first_name
                last_name = model_instance.last_name

                # Check if a user with the first name and last name exists
                user, created = User.objects.get_or_create(
                    first_name=first_name,
                    last_name=last_name,
                    defaults={'username': f'{first_name.lower()}.{last_name.lower()}'}
                )

                if created:
                    # Set a default password for the newly created user
                    user.set_password('defaultpassword')
                    user.save()

                # Create a new Report record for the check-in
                Report.objects.create(
                    user=user,
                    area=area,
                    class_model=class_model,
                    code=code,
                    arrival_time=timezone.now()
                )

                # Associate the user with the area if not already associated
                if not area.users.filter(id=user.id).exists():
                    area.users.add(user)
                    messages.success(request, f'Successfully checked into {area.area_of_use} with name {first_name} {last_name}')
                else:
                    messages.info(request, f'The name {first_name} {last_name} is already checked into {area.area_of_use}')
            except ModelTest.DoesNotExist:
                messages.error(request, 'Invalid code. Please enter a valid code.')
            return redirect('report:check-in')
    else:
        form = CheckInForm()
    return render(request, 'report/check_in.html', {'form': form})


def check_out(request):
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data.get('area')
            code = form.cleaned_data.get('code')
            try:
                model_instance = ModelTest.objects.get(code=code)
                first_name = model_instance.first_name
                last_name = model_instance.last_name

                # Find the user with the first name and last name
                user = User.objects.get(first_name=first_name, last_name=last_name)

                # Find the latest Report record for the user and update the departure time
                report = Report.objects.filter(user=user, area=area, code=code).order_by('-arrival_time').first()
                if report and not report.departure_time:
                    report.departure_time = timezone.now()
                    report.save()

                     # Remove the user from the area
                    area.users.remove(user)
                    messages.success(request, f'Successfully checked out of {area.area_of_use} with name {first_name} {last_name}')
                else:
                    messages.info(request, f'The name {first_name} {last_name} is not currently checked into {area.area_of_use}')
            except (ModelTest.DoesNotExist, User.DoesNotExist):
                messages.error(request, 'Invalid code or user does not exist. Please enter a valid code.')
            return redirect('report:check-out')
    else:
        form = CheckOutForm()
    return render(request, 'report/check_out.html', {'form': form})