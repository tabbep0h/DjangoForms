from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    return render(request, "index.html")


def appointment(request):
    name = request.POST.get("name", "Undefined")
    phone = request.POST.get("phone", "Undefined")
    email = request.POST.get("email", "Undefined")
    service = request.POST.get("service", "Undefined")
    about = request.POST.get("about", "Undefined")
    return HttpResponse(f"""
            <p>ФИО: {name}</p>
            <p>Номер: {phone}</p>
            <p>Почта: {email}</p>
            <p>Тип: {service}</p>
            <p>Рассказ: {about}</p>
""")


def ordermain(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        second_name = request.POST.get('second_name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        street = request.POST.get('street')
        street_number = request.POST.get('street_number')
        home_number = request.POST.get('home_number ')
        return HttpResponse(f"""
                           <h2>{name} {second_name}, проверьте адрес доставки:</h2>
                           <p>{country}</p>
                           <p>{city}</p>
                           <p>{street} {street_number}</p>
                           <p>{home_number}</p>
                            """)
    else:
        userform = UserForm()
        return render(request, "ordermain.html", context={"form": userform})
