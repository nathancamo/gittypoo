import flet as ft

def main(page: ft.Page):
    page.title = "Glassmorphic Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # We need a vibrant background so the glass effect is actually visible
    # You can swap this URL with a local image pathway later!
    background_image = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1080&auto=format&fit=crop"

    # --- Reusable Glass Container Style ---
    def glass_card(content_widget):
        return ft.Container(
            content=content_widget,
            width=page.width,
            padding=20,
            border_radius=25,
            # The Magic of Glassmorphism:
            bgcolor=ft.colors.with_opacity(0.08, ft.colors.WHITE), # Semi-transparent white
            blur=ft.Blur(15, 15, ft.BlurTileMode.MIRROR),          # Frosted blur effect
            border=ft.border.all(1.5, ft.colors.with_opacity(0.15, ft.colors.WHITE)), # Thin, light border for the glass edge
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK),
                offset=ft.Offset(0, 5)
            )
        )

    # --- Widget 1: Pet Care Tracker ---
    pet_tracker = ft.Column([
        ft.Text("Fur Family", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Divider(color=ft.colors.with_opacity(0.2, ft.colors.WHITE)),
        ft.ListTile(
            leading=ft.Icon(ft.icons.PETS, color=ft.colors.WHITE),
            title=ft.Text("Cooper (Tuxedo)", color=ft.colors.WHITE),
            subtitle=ft.Text("Fed at 7:00 AM", color=ft.colors.WHITE70),
            trailing=ft.IconButton(ft.icons.CHECK_CIRCLE_OUTLINE, icon_color=ft.colors.WHITE)
        ),
        ft.ListTile(
            leading=ft.Icon(ft.icons.PETS, color=ft.colors.WHITE),
            title=ft.Text("Luna (Ragdoll)", color=ft.colors.WHITE),
            subtitle=ft.Text("Fed at 7:00 AM", color=ft.colors.WHITE70),
            trailing=ft.IconButton(ft.icons.CHECK_CIRCLE_OUTLINE, icon_color=ft.colors.WHITE)
        )
    ], spacing=5)

    # --- Widget 2: Network & Server Node ---
    network_node = ft.Column([
        ft.Text("Home Network", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Divider(color=ft.colors.with_opacity(0.2, ft.colors.WHITE)),
        ft.Row([
            ft.Icon(ft.icons.DNS, color=ft.colors.GREEN_400),
            ft.Text("AdGuard Home: Active", color=ft.colors.WHITE, weight=ft.FontWeight.W_500)
        ], alignment=ft.MainAxisAlignment.START),
        ft.Container(height=10),
        ft.Row([
            ft.Icon(ft.icons.VPN_KEY, color=ft.colors.BLUE_400),
            ft.Text("Tailscale Tunnel: Connected", color=ft.colors.WHITE, weight=ft.FontWeight.W_500)
        ], alignment=ft.MainAxisAlignment.START)
    ])

    # --- Main Page Layout ---
    main_layout = ft.Container(
        image_src=background_image,
        image_fit=ft.ImageFit.COVER,
        expand=True,
        padding=20,
        content=ft.SafeArea(
            content=ft.Column([
                glass_card(pet_tracker),
                ft.Container(height=20), # Spacer
                glass_card(network_node)
            ])
        )
    )

    page.add(main_layout)

ft.app(target=main)
