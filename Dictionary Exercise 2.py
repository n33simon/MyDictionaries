filename = "WorldSeriesWinners.txt"
roster = {}
series_record = {}
index = 1903


def main():
    # create lines
    lines = create_lines()

    # prompt user
    winner_record = int(
        input("What year would you like to know the World Series Winner? ")
    )

    # create dictionary 1
    records = dict_1(lines)

    # create dictionary 2
    series = dict_2(lines, index)

    # get Series and Record finding
    output()


def create_lines():
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.insert(1, "No winner")
        lines.insert(88, "No winner")
    return lines


def dict_1(lines):
    for line in lines:
        if line not in roster:
            roster[line] = lines.count(line)
    print(roster)
    return roster


def dict_2(lines, index):
    for line in lines:
        if index not in series_record:
            series_record[index] = line
            index += 1
    return series_record
    print(series_record)


def output(winner_record, roster, series_record):
    winner = series_record.get(winner_record)
    record = roster.get(winner)
    return winner
    return record

    # print(lines)
    print(winner)
    print(record)
    main()
