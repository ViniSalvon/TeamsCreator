from random import randint
import input_data as data


def create_groups(lists_number):
    if isinstance(lists_number, int):
        return [[] for _ in range(lists_number)]    # lists_number = 4 will return [[], [], [], []]
    else:
        raise TypeError('Input should be integer.')


def check_data(number, lista):
    # Check if data type is correct
    if not ((isinstance(number, int)) or (isinstance(lista, list))):
        raise TypeError('Input data incorrect. TEAMS_LIST should be a list and GROUPS_NUMBER should be integer.')

    # Check if number of teams or number of groups is not equal or less than zero
    if (number <= 0) or (len(lista) == 0):
        raise ValueError("List of teams should have at least one team. Number of groups shouldn't be zero or negative.")

    # Check if there is consistency between number of groups and number of teams
    if number > len(lista):
        raise ValueError("It shouldn't have more groups than teams")

    if len(lista) % number != 0:
        print(
            "WARNING: The number of teams is not divisible by the number of groups. "
            "The program will run normally, but some groups will have more teams than others."
        )
        input("Press enter to continue.")


def main():
    # Check input data
    check_data(data.GROUPS_NUMBER, data.TEAMS_LIST)

    # Create lists
    final_list = create_groups(data.GROUPS_NUMBER)  # Groups lists
    main_list = data.TEAMS_LIST.copy()

    # Iterations, main program a.k.a. "Onde a magia acontece"
    while len(main_list) > 0:       # It will stop when there is no more teams to be sorted
        for current_group in range(len(final_list)):  # Randomly adds a team to each group while removing from main list

            if len(main_list) == 0:     # Test if list is already empty.
                break

            position = randint(0, (len(main_list) - 1))     # Select a random position from list
            choosen_team = main_list.pop(position)          # Remove item in the given position

            final_list[current_group].append(choosen_team)  # Add item to a group

    # Afterwards, prints everything to console
    for index, lista in enumerate(final_list):
        print('Group', (index + 1))
        print(lista)
        print('\n')

    print('Grupos criados com sucesso.')


if __name__ == '__main__':
    main()

