from django.urls import path

from .views import (add, add_pendidikan_pekerjaan, delete_pekerjaan,
                    delete_pendidikan, detail, detele, edit,
                    edit_delete_pekerjaan, edit_delete_pendidikan, index)

app_name = "person"


urlpatterns = [
    path(route="", view=index, name="index"),

    path(route="<int:id>/", view=detail, name="detail"),

    path(route="add/", view=add, name="add"),
    path(
        route="add/<int:id>",
        view=add_pendidikan_pekerjaan,
        name="add_pendidikan_pekerjaan"
    ),
    path(
        route="add_delete_pendidikan/<int:person_id>/<int:pendidikan_id>",
        view=delete_pendidikan,
        name="delete_pendidikan"
    ),
    path(
        route="add_delete_pekerjaan/<int:person_id>/<int:pekerjaan_id>",
        view=delete_pekerjaan,
        name="delete_pekerjaan"
    ),


    path(route="edit/<int:id>", view=edit, name="edit"),
    path(
        route="edit_delete_pendidikan/<int:person_id>/<int:pendidikan_id>",
        view=edit_delete_pendidikan,
        name="edit_delete_pendidikan"
    ),
    path(
        route="edit_delete_pekerjaan/<int:person_id>/<int:pekerjaan_id>",
        view=edit_delete_pekerjaan,
        name="edit_delete_pekerjaan"
    ),

    path(route="delete/<int:id>", view=detele, name="delete"),

]
