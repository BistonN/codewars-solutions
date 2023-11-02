def sum_of_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    total_length = 0
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total_length += current_end - current_start
            current_start, current_end = start, end

    total_length += current_end - current_start
    return total_length