def add_guests(
    guests: list[str],
    new_guests: list[str]
) -> list[str]:
    atualizar_listas = guests.copy()
    atualizar_listas.extend(new_guests)
    return atualizar_listas