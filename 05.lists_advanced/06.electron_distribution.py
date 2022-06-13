def electron_distribution(electrons):
    shell_position = 1
    shell_distribution = []
    while True:
        max_num_of_electrons = 2 * (shell_position ** 2)

        if electrons > max_num_of_electrons:
            electrons -= max_num_of_electrons
            shell_distribution.append(max_num_of_electrons)

        else:
            shell_distribution.append(electrons)
            break

        shell_position += 1

    print(shell_distribution)


num_of_electrons = int(input())
electron_distribution(num_of_electrons)