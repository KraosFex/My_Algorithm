



# Esta es la menera correcta de generar un menu,
# Esto se hace asi para evitar pasar muchos argumentos a un solo metodo
from dataclasses import dataclass, astuple

@dataclass
class MenuConfing:
    """A configuration for the Menu.
    
    Atributes:
        title: The title of the Menu.
        body: The body of the Menu.
        buttton_text: The text for rhe button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool = False
    
def create_menu(config: MenuConfing) -> any:
    title, body, button_text, cancallable = astuple(config)

create_menu(
    MenuConfing(
        title="My delicious menu",
        body="A description",
        button_text="order Now!"
    )
)