import flet as fl


def panel_creator_classesgroups(page: fl.Page):

    input_group_name = fl.TextField(
        label="Nombre del grupo",
        hint_text=None,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=180,
        height=50,
        text_size=13,
    )

    input_group_profesor = fl.TextField(
        label="Profesores (opcional)",
        hint_text=None,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=220,
        height=50,
        text_size=13,
    )

    addgroup_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#4CAF50",
        color="white",
        height=45,
    )

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
                    input_group_profesor,
                    addgroup_button,
                ],
                spacing=10,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )

    return fl.Container(
        content=fl.Column(
            controls=[
                header_grupos,
                fl.Divider(height=10, color="#3D3D3D"),
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
