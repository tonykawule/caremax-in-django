from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Registration and Login views


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'patient/home.html')

## PATIENT BLOCK ##

# create a patient


@login_required(login_url='login')
def newpatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'f {{ patient }} added successfully')
        return redirect('patientlist')

    context = {'form': form}

    return render(request, 'patient/newpatient.html', context)

# read created patients


@login_required(login_url='login')
def patientlist(request):
    patients = Patient.objects.all()

    context = {'patients': patients}

    return render(request, 'patient/patient_list.html', context)


# Edit patient
@login_required(login_url='login')
def editpatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'f {{ Patient }} updated successfully')
        return redirect('patientlist')

    context = {'form': form}

    return render(request, 'patient/editpatient.html', context)

# Delete patient


@login_required(login_url='login')
def deletepatient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'f {{ Patient }} deleted successfully')
        return redirect('patientlist')
    context = {'patient': patient}
    return render(request, 'patient/deletepatient.html', context)

# patient profile


@login_required(login_url='login')
def profile(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    visits = Patient.objects.get(id=patient_id)
    tests = Patient.objects.get(id=patient_id)
    treatments = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'visits': visits,
               'tests': tests, 'treatments': treatments}
    return render(request, 'patient/profile.html', context)


## Visit BLOCK ####

# create patient visit
@login_required(login_url='login')
def newpatientvisit(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = VisitForm()
    if request.method == 'POST':
        form = VisitForm(request.POST, patient_id)
        if form.is_valid():
            form.save()
            return redirect('visitlist', patient_id=patient.id)
    context = {'patient': patient, 'form': form}

    return render(request, 'visit/addvisit.html', context)


# read patient visits
@login_required(login_url='login')
def visitlist(request, patient_id):
    visits = Patient.objects.get(id=patient_id)
    context = {'visits': visits}
    return render(request, 'visit/visitlist.html', context)

# edit patient visit


@login_required(login_url='login')
def editpatientvisit(request, patient_id, pk):
    visit = Visit.objects.get(pk)
    form = VisitForm(instance=visit)

    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
        return redirect('visitlist')

    context = {'form': form}

    return render(request, 'visit/editvisit.html', context)


# Tests Block
@login_required(login_url='login')
def newpatienttest(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST, patient_id)
        if form.is_valid():
            form.save()
            return redirect('testlist', patient_id=patient.id)
    context = {'patient': patient, 'form': form}

    return render(request, 'test/addtest.html', context)


# read patient test
@login_required(login_url='login')
def testlist(request, patient_id):
    tests = Patient.objects.get(id=patient_id)
    context = {'tests': tests}
    return render(request, 'test/testlist.html', context)


# Treatment Block
@login_required(login_url='login')
def newpatienttreatment(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = TreatmentForm()
    if request.method == 'POST':
        form = TreatmentForm(request.POST, patient_id)
        if form.is_valid():
            form.save()
            return redirect('treatmentlist', patient_id=patient.id)
    context = {'patient': patient, 'form': form}

    return render(request, 'treatment/addtreatment.html', context)


# read patient treatment
@login_required(login_url='login')
def treatmentlist(request, patient_id):
    treatments = Patient.objects.get(id=patient_id)
    context = {'treatments': treatments}
    return render(request, 'treatment/treatmentlist.html', context)

# Bill block


@login_required(login_url='login')
def newpatientbill(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = BillForm()
    if request.method == 'POST':
        form = BillForm(request.POST, patient_id)
        if form.is_valid():
            form.save()
            return redirect('bill_list', patient_id=patient.id)
    context = {'patient': patient, 'form': form}

    return render(request, 'bill/new.html', context)

# Bill List


@login_required(login_url='login')
def bill_list(request, patient_id):
    bills = Patient.objects.get(id=patient_id)
    context = {'bills': bills}
    return render(request, 'bill/bill_list.html', context)


##  Stock Category ##

@login_required(login_url='login')
def newstockcategory(request):
    form = StockcategoryForm()
    if request.method == 'POST':
        form = StockcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock Category added successfully')
        return redirect('stockcategorylist')

    context = {'form': form}

    return render(request, 'stockcategory/newstockcategory.html', context)

## read stock category ##


@login_required(login_url='login')
def stockcategorylist(request):
    stockcategories = Stockcategory.objects.all()

    context = {'stockcategories': stockcategories}

    return render(request, 'stockcategory/stockcategorylist.html', context)

# Edit stockcategory


@login_required(login_url='login')
def editstockcategory(request, pk):
    stockcategory = Stockcategory.objects.get(id=pk)
    form = StockcategoryForm(instance=stockcategory)

    if request.method == 'POST':
        form = StockcategoryForm(request.POST, instance=stockcategory)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'f {{ Stockcategory }} updated successfully')
        return redirect('stockcategorylist')

    context = {'form': form}

    return render(request, 'stockcategory/editstockcategory.html', context)

# Delete Inventory


@login_required(login_url='login')
def deletestockcategory(request, pk):
    stockcategories = Stockcategory.objects.get(id=pk)
    if request.method == 'POST':
        stockcategories.delete()
        messages.success(request, 'f {{ stockcategory }} deleted successfully')
        return redirect('stockcategorylist')
    context = {'stockcategories': stockcategories}
    return render(request, 'stockcategory/deletestockcategory.html', context)


## End of stock category ##

## STOCK ##

@login_required(login_url='login')
def newstock(request):
    stock = Stock.objects.all()
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'f {{stock}} added successfully')
        return redirect('stocklist')

    context = {'form': form, 'stock': stock}

    return render(request, 'stock/newstock.html', context)

# read created inventory


@login_required(login_url='login')
def stocklist(request):
    stocks = Stock.objects.all()

    context = {'stocks': stocks}

    return render(request, 'stock/stocklist.html', context)

## edit stock ##


@login_required(login_url='login')
def editstock(request, pk):
    stocks = Stock.objects.get(id=pk)
    form = StockForm(instance=stocks)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stocks)
        if form.is_valid():
            form.save()
            messages.success(
                request, '{{ Stock.item_name }} updated successfully')
        return redirect('stocklist')

    context = {'form': form}

    return render(request, 'stock/editstock.html', context)

## delete stock ##


@login_required(login_url='login')
def deletestock(request, pk):
    stocks = Stock.objects.get(id=pk)
    if request.method == 'POST':
        stocks.delete()
        messages.success(request, 'f {{ stocks }} deleted successfully')
        return redirect('stocklist')
    context = {'stocks': stocks}
    return render(request, 'stock/deletestock.html', context)

## stock detail view ##


@login_required(login_url='login')
def stock_detail(request, pk):
    stocks = Stock.objects.get(id=pk)
    context = {'stocks': stocks}
    return render(request, 'stock/stockdetail.html', context)

## Issue stock item ##


@login_required(login_url='login')
def issue_item(request, pk):
    stocks = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=stocks)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issued_quantity
        messages.success(request, "{{ stock.item_name }} Issued successfully")
        instance.save()
        return redirect('stocklist')

    context = {'stock': stocks,
               'form': form}
    return render(request, 'stock/issue_item.html', context)

## Receive stock item ##


@login_required(login_url='login')
def receive_item(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.quantity_received
        messages.success(request, "Received successfully")
        instance.save()
        return redirect('stocklist')

    context = {'instance': queryset,
               'form': form}
    return render(request, 'stock/receive_item.html', context)

## Reorder level view ##


@login_required(login_url='login')
def reorder_level(request, pk):
    stocks = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=stocks)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, "Reoder level set successfully for")
        instance.save()
        return redirect('stocklist')

    context = {'instance': stocks,
               'form': form}
    return render(request, 'stock/receive_item.html', context)
