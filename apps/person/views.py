from django.shortcuts import redirect, render

from .models import Pendidikan, PengalamanKerja, Person

# Create your views here.


def index(request):
    data = Person.objects.all().order_by("-id")

    context = {"data": data}

    return render(request=request, template_name="person/index.html", context=context)


def add(request):

    if request.method == "POST":
        data = Person.objects.create(
            nama=request.POST["nama"],
            ktp=request.POST["ktp"],
            alamat=request.POST["alamat"],
            image=request.FILES['foto']
        )
        data.save()
        return redirect(to="person:add_pendidikan_pekerjaan", id=data.id)

    return render(request=request, template_name="person/add.html", context={})


def add_pendidikan_pekerjaan(request, id):
    person = Person.objects.get(id=id)

    if request.method == "POST":
        if "add_pendidikan" in request.POST:
            pendidikan = Pendidikan.objects.create(
                nama=request.POST["sekolah"],
                jurusan=request.POST["jurusan"],
                tahun_masuk=request.POST["tahun_masuk"],
                tahun_lulus=request.POST["tahun_lulus"],
                person_id=person.id,
            )
            pendidikan.save()
        if "add_pekerjaan" in request.POST:
            pekerjaan = PengalamanKerja.objects.create(
                perusahaan=request.POST["perusahaan"],
                jabatan=request.POST["jabatan"],
                tahun=request.POST["tahun"],
                keterangan=request.POST["keterangan"],
                person_id=person.id,
            )
            pekerjaan.save()
        if "finish" in request.POST:
            return redirect(to="person:index")

    pendidikan = Pendidikan.objects.filter(person_id=person.id)
    pekerjaan = PengalamanKerja.objects.filter(person_id=person.id)

    context = {
        "person": person,
        "pendidikan": pendidikan,
        "pekerjaan": pekerjaan,
    }

    return render(request=request, template_name="person/add_pendidikan_pekerjaan.html", context=context)


def delete_pendidikan(request, person_id, pendidikan_id):
    Pendidikan.objects.filter(id=pendidikan_id).delete()
    return redirect(to="person:add_pendidikan_pekerjaan", id=person_id)


def delete_pekerjaan(request, person_id, pekerjaan_id):
    PengalamanKerja.objects.filter(id=pekerjaan_id).delete()
    print("\n\nSempet kesini\n\n")
    return redirect(to="person:add_pendidikan_pekerjaan", id=person_id)


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
    person = Person.objects.get(id=id)
    pendidikan = Pendidikan.objects.filter(person_id=id)
    pekerjaan = PengalamanKerja.objects.filter(person_id=id)

    if request.method == "POST":
        if "add_pendidikan" in request.POST:
            pendidikan = Pendidikan.objects.create(
                nama=request.POST["sekolah"],
                jurusan=request.POST["jurusan"],
                tahun_masuk=request.POST["tahun_masuk"],
                tahun_lulus=request.POST["tahun_lulus"],
                person_id=person.id,
            )
            pendidikan.save()
            return redirect(to="person:edit", id=person.id)
        if "add_pekerjaan" in request.POST:
            pekerjaan = PengalamanKerja.objects.create(
                perusahaan=request.POST["perusahaan"],
                jabatan=request.POST["jabatan"],
                tahun=request.POST["tahun"],
                keterangan=request.POST["keterangan"],
                person_id=person.id,
            )
            pekerjaan.save()
            return redirect(to="person:edit", id=person.id)
        if "finish" in request.POST:
            person.nama = request.POST["nama"]
            person.ktp = request.POST["ktp"]
            person.alamat = request.POST["alamat"]
            person.image = request.FILES['foto']
            person.save()
            return redirect(to="person:index")

    context = {
        "person": person,
        "pendidikan": pendidikan,
        "pekerjaan": pekerjaan
    }

    return render(request=request, template_name="person/edit.html", context=context)


def edit_delete_pendidikan(request, person_id, pendidikan_id):
    Pendidikan.objects.filter(id=pendidikan_id).delete()
    return redirect(to="person:edit", id=person_id)


def edit_delete_pekerjaan(request, person_id, pekerjaan_id):
    PengalamanKerja.objects.filter(id=pekerjaan_id).delete()
    return redirect(to="person:edit", id=person_id)


def detele(request, id):
    Person.objects.filter(id=id).delete()
    return redirect(to="person:index")
