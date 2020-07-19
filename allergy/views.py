from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.utils import timezone
from .forms import AllergyForm
from .models import Allergy
from .models import Hospitalization
from .forms import HospitalizationForm





def registerform(request):
    if request.method == 'GET':
        return render(request, 'allergy/registerform.html', {'form': UserCreationForm()})
    else:
        # can move to controller
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'allergy/registerform.html', {
                    'form': UserCreationForm(),
                    'errMsg': 'User exists. choose a different one'
                })
        else:
            print('error message - Type mismatch')
            return render(request, 'allergy/registerform.html', {
                'form': UserCreationForm(),
                'errMsg': 'Password did not match'
            })


def logoutuser(request):
    if request.method == 'POST' :
        logout(request)
        return redirect('homepage')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'allergy/loginform.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'allergy/loginform.html',
                          {'form': AuthenticationForm(), 'errMsg': 'user does not exits'})
        else:
            login(request, user)
            return redirect('profile')


def homepage(request):
    return render(request, 'allergy/index.html')            


def index(request):
    return render(request, 'allergy/index.html') 

@login_required()
def profile(request):
    allergies = Allergy.objects.filter(user_id=request.user, dateCompleted__isnull=True).order_by('-dateCreated')
    return render(request, 'allergy/profile.html', {'allallergies': allergies})



@login_required()
def createNewAllergy(request):
    if request.method == 'GET':
        return render(request, 'allergy/createNewAllergy.html', {'form': AllergyForm()})
    else:
        try:
            form = AllergyForm(request.POST)
            newallergy = form.save(commit=False)
            newallergy.user_id = request.user
            newallergy.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'allergy/createNewAllergy.html', {'form': AllergyForm(), 'errMsg': 'Data mismatch'})
    


def Emergency(request):
    return render(request, 'allergy/Emergency.html')  

    

def json(request):
    return render(request, 'allergy/json.html')

def createNewHospitalization(request):
    if request.method == 'GET':
        return render(request, 'allergy/createNewHospitalization.html', {'form': HospitalizationForm()})
    else:
        try:
            form = HospitalizationForm(request.POST)
            newhospitalization = form.save(commit=False)
            newhospitalization.user_id = request.user
            newhospitalization.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'allergy/createNewHospitalization.html', {'form': HospitalizationForm(), 'errMsg': 'Data mismatch'})  


@login_required
def updateallergy(request, allergy_pk):
    allergy = get_object_or_404(Allergy, pk=allergy_pk, user_id=request.user)
    if request.method == 'GET':
        form = AllergyForm(instance=allergy)
        return render(request, 'allergy/updateallergy.html', {'allergy': allergy,'form': form})
    else:
        try:
            form = AllergyForm(request.POST, instance=allergy)
            form.save()
            return redirect('profile')
        except ValueError:
              return render(request, 'allergy/updateallergy.html', {'form': AllergyForm(), 'errMsg': "Data mismatch"})



@login_required
def deleteallergy(request, allergy_pk):
    allergy = get_object_or_404(Allergy, pk=allergy_pk, user_id=request.user)
    if request.method == 'POST':
        allergy.delete()
        return redirect('profile') 



@login_required
def doneallergy(request, allergy_pk):
    allergy = get_object_or_404(Allergy, pk=allergy_pk, user_id=request.user)
    if request.method == 'POST':
        allergy.dateCompleted = timezone.now()
        allergy.save()
        return redirect('profile')


