from django.shortcuts import render, redirect

from .models import Pendidikan, PengalamanKerja, Person

# Create your views here.


def index(request):
    data = Person.objects.all().order_by("-id")
    # max_id = Person.objects.latest("id").id + 1
    context = {"data": data}

    return render(request=request, template_name="person/index.html", context=context)


def add(request):
    temp_person = Person(nama="Draft", ktp="Draft", alamat="Draft")
    # temp_person.save()
    # person = Person()
    # person.id = 2
    print("\n\n", temp_person.id, "\n\n")
    # pedidikan = Pendidikan(request.POST or None)
    # pengalaman_kerja = PengalamanKerja(request.POST or None)

    if request.method == "POST":
        person = Person.objects.get(id=temp_person.id)
        person.nama = "bukan draft"
        person.save()
        # person = Person.objects.create(
        #     nama=request.POST["nama"],
        #     ktp=request.POST["ktp"],
        #     alamat=request.POST["alamat"],
        # )
        # person.save()

        # if data.is_valid():
        #     data.save()
        #     return redirect(to="kontak:index")
        return redirect(to="person:index")
    # print("\n\n", person.id, "\n\n")

    context = {"data": None}

    return render(request=request, template_name="person/add.html", context=context)


def detail(request, id):
    person = Person.objects.get(id=id)
    pendidikan = Pendidikan.objects.filter(person_id=id)
    pengalaman_kerja = PengalamanKerja.objects.filter(person_id=id)

    context = {
        "person": person,
        "pendidikan": pendidikan,
        "pengalaman_kerja": pengalaman_kerja,
    }

    return render(request=request, template_name="person/detail.html", context=context)


def edit(request, id):
    # model = KontakModel.objects.get(id=id)

    # initial = {
    #     "nama": model.nama,
    #     "email": model.email,
    #     "gender": model.gender,
    #     "phone": model.phone,
    #     "alamat": model.alamat,
    # }

    # data = KontakForm(
    #     data=request.POST or None,
    #     initial=initial,
    #     instance=model
    # )

    # if request.method == "POST":
    #     if data.is_valid():
    #         data.save()
    #         return redirect(to="kontak:detail", id=model.id)

    # context = {"data": data}

    return render(request=request, template_name="person/edit.html", context={})


def detele(request, id):
    Person.objects.filter(id=id).delete()
    return redirect(to="person:index")
