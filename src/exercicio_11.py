def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    atualizar_listas = guests.copy()

    if unavailable in atualizar_listas:
        index = atualizar_listas.index(unavailable)
        atualizar_listas[index] =new_guest

    return atualizar_listas

