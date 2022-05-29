def race_winner(time):
    times_to_finish = len(time_for_both) // 2
    times_left = []
    times_right = []
    for t_l in range(times_to_finish):
        times_left.append(time_for_both[t_l])

    for t_r in range(times_to_finish):
        times_right.append(time_for_both[-1])
        time_for_both.pop(-1)

    tot_time_left = 0
    tot_time_right = 0

    for l in times_left:
        if l == 0:
            tot_time_left -= tot_time_left * 0.20
        tot_time_left += l

    for r in times_right:
        if r == 0:
            tot_time_right -= tot_time_right * 0.20
        tot_time_right += r
    if tot_time_left < tot_time_right:
        print(f"The winner is left with total time: {tot_time_left:.1f}")
    else:
        print(f"The winner is right with total time: {tot_time_right:.1f}")


time_for_both = list(map(int, input().split(" ")))
race_winner(time_for_both)
