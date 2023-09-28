from django.urls import path

from .views import (add, add_pendidikan_pekerjaan, delete_pekerjaan,
                    delete_pendidikan, detail, detele, edit, index)

app_name = "person"


urlpatterns = [
    path(route="", view=index, name="index"),

    path(route="add/", view=add, name="add"),
    path(
        route="add/<int:id>",
        view=add_pendidikan_pekerjaan,
        name="add_pendidikan_pekerjaan"
    ),
    path(
        route="add/<int:person_id>/<int:pendidikan_id>",
        view=delete_pendidikan,
        name="delete_pendidikan"
    ),
    path(
        route="add/<int:person_id>/<int:pekerjaan_id>",
        view=delete_pekerjaan,
        name="delete_pekerjaan"
    ),

    path(route="<int:id>/", view=detail, name="detail"),
    path(route="edit/<int:id>", view=edit, name="edit"),
    path(route="delete/<int:id>", view=detele, name="delete"),

]
