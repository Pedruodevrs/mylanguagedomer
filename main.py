import flet as ft

def main(page: ft.Page):
    # Configurações de estilo (App Independente)
    page.title = "DOMER SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0a0a0a"  # Fundo preto estilo terminal
    page.padding = 20

    # Função para ler o seu arquivo .dom original
    def ler_dom():
        try:
            with open("script.dom", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: Arquivo script.dom não encontrado!"

    # Interface do Usuário
    page.add(
        ft.Column([
            ft.Row([
                ft.Icon(ft.icons.SHIELD_MOON, color="green", size=40),
                ft.Text("DOMER MOBILE", size=24, weight="bold", color="green"),
            ], alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Divider(color="green", height=30),
            
            ft.Text("LOG DO SISTEMA .DOM:", size=14, color="white70"),
            
            # Área que mostra o conteúdo do seu .dom
            ft.Container(
                content=ft.Text(ler_dom(), font_family="monospace", color="#33ff33"),
                bgcolor="#1a1a1a",
                padding=15,
                border_radius=10,
                border=ft.border.all(1, "green"),
                expand=True
            ),
            
            ft.ElevatedButton(
                "EXECUTAR COMANDO", 
                icon=ft.icons.PLAY_ARROW,
                style=ft.ButtonStyle(color="black", bgcolor="green"),
                on_click=lambda _: print("Comando executado!")
            )
        ], expand=True)
    )

# Esse comando prepara o app para rodar no navegador do celular
if __name__ == "__main__":
    ft.app(target=main)
  
