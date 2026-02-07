# grupos.py
import flet as fl
from data import temp_save


def panel_creator_classesgroups(page: fl.Page):

    # ╔¤═══════¤GRUPOS AGREGADOS¤════════¤╗
    grupos_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_grupo(grupo_name):
        def handler(e):
            temp_save.remove_grupo(grupo_name)
            for control in grupos_list.controls:
                if control.data == grupo_name:
                    grupos_list.controls.remove(control)
                    break
            page.update()

        return handler

    def create_onlist_grupo(grupo):
        return fl.Container(
            data=grupo.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.GROUP, color="#4CAF50"),
                            fl.Text(
                                grupo.name,
                                size=16,
                                weight=fl.FontWeight.W_500,
                                color="white",
                            ),
                        ],
                        spacing=10,
                    ),
                    fl.IconButton(
                        icon=fl.Icons.DELETE,
                        icon_color="#F44336",
                        icon_size=20,
                        tooltip="Eliminar grupo",
                        on_click=fl_delete_grupo(grupo.name),
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤GRUPOS AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_group_name = fl.TextField(
        label="Nombre del grupo",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    def fl_add_grupo(e):
        if not input_group_name.value:
            return

        grupo = temp_save.add_grupo(name=input_group_name.value)
        grupos_list.controls.append(create_onlist_grupo(grupo))
        input_group_name.value = ""
        page.update()

    addgroup_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#4CAF50",
        color="white",
        height=45,
        on_click=fl_add_grupo,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_grupos = fl.Row(
        controls=[
            fl.Text(
                "🎓 Grupos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_group_name,
                    addgroup_button,
                ],
                spacing=10,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )
    # ╚¤═══════¤HEADER¤════════¤╝

    return fl.Container(
        content=fl.Column(
            controls=[
                header_grupos,
                fl.Divider(height=10, color="#3D3D3D"),
                grupos_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
