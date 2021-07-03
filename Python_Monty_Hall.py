import secrets


def get_game_result(change: bool, num_doors: int) -> int:

    # 0 is empty
    # 1 is the prize
    doors = [0 for x in range(num_doors)]
    doors[0] = 1

    choice = secrets.choice(doors)

    if choice == 1:
        if change:
            return 0
        else:
            return 1

    else:
        if change:

            doors.pop(doors.index(choice))
            # Monty removed an empty door
            doors.remove(0)

            new_choice = secrets.choice(doors)

            if new_choice == 1:
                return 1
            else:
                return 0
        else:
            return 0


def get_num_wins(change: bool, tries: bool, num_doors: int) -> int:

    wins_count = 0

    for t in range(tries):
        result = get_game_result(change, num_doors)
        wins_count += result

    return wins_count


if __name__ == "__main__":

    num_doors = int(input("Quantidade de portas\n-> "))
    repeticoes = int(input("Quantidade de jogos\n-> "))

    result_change = get_num_wins(True, repeticoes, num_doors)
    result_not_change = get_num_wins(False, repeticoes, num_doors)

    print(f"Acertos ao trocar a porta: {(result_change / repeticoes)*100}%")
    print(f"Acertos ao manter a porta: {(result_not_change / repeticoes)*100}%")
