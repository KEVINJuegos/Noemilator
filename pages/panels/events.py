import flet as fl

DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def panel_creator_events(page: fl.Page):

    # ╔¤═══════¤TURNOS LIST¤════════¤╗
    turnos_list = fl.Column(
        controls=[],
        spacing=5,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    # ╚¤═══════¤TURNOS LIST¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    dropdown_dia_inicio = fl.Dropdown(
        label="Día Inicio",
        value="Lunes",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=140,
        text_size=13,
        options=[fl.dropdown.Option(d) for d in DAYS],
    )

    dropdown_dia_fin = fl.Dropdown(
        label="Día Fin",
        value="Viernes",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=140,
        text_size=13,
        options=[fl.dropdown.Option(d) for d in DAYS],
    )

    apply_days_button = fl.ElevatedButton(
        text="Aplicar",
        icon=fl.Icons.CHECK,
        bgcolor="#4CAF50",
        color="white",
        height=45,
    )

    add_turno_button = fl.ElevatedButton(
        text="+ Agregar Turno",
        bgcolor="#FF9800",
        color="white",
        height=45,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤CONFIG PANEL¤════════¤╗
    turnos_panel = fl.Container(
        content=fl.Column(
            controls=[
                fl.Text(
                    "⚙️ Configuración",
                    size=18,
                    weight=fl.FontWeight.BOLD,
                    color="white",
                ),
                fl.Divider(height=10, color="#3D3D3D"),
                fl.Text(
                    "📅 Rango de Días",
                    size=14,
                    color="white",
                ),
                fl.Row(
                    controls=[
                        dropdown_dia_inicio,
                        fl.Text(
                            "→",
                            size=16,
                            color="white",
                        ),
                        dropdown_dia_fin,
                    ],
                    spacing=10,
                    vertical_alignment=fl.CrossAxisAlignment.CENTER,
                ),
                apply_days_button,
                fl.Divider(height=10, color="#3D3D3D"),
                fl.Row(
                    controls=[
                        fl.Text(
                            "⏰ Turnos",
                            size=14,
                            color="white",
                        ),
                        add_turno_button,
                    ],
                    alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=fl.CrossAxisAlignment.CENTER,
                ),
                fl.Container(
                    content=turnos_list,
                    expand=True,
                    padding=10,
                    border=fl.border.all(1, "#3D3D3D"),
                    border_radius=8,
                ),
            ],
            spacing=10,
            expand=True,
        ),
        width=350,
        padding=15,
        bgcolor="#1E1E1E",
        border_radius=10,
    )
    # ╚¤═══════¤CONFIG PANEL¤════════¤╝

    return fl.Container(
        content=fl.Row(
            controls=[turnos_panel],
            alignment=fl.MainAxisAlignment.START,
            vertical_alignment=fl.CrossAxisAlignment.START,
        ),
        padding=20,
        expand=True,
    )
