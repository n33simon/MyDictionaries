filename = "WorldSeriesWinners.txt"
roster = {}
series_record = {}
index = 1903


def main():
    # create lines
    lines = create_lines()

    # create dictionary 1
    records = dict_1(lines, winner_record)

    # create dictionary 2
    series = dict_2(lines, index, winner_record)

    # get Series and Record finding
    output()

    # prompt user
    winner_record = input("Year? ")
    input = int(winner_record)
    print({winner_record})


def create_lines():
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.insert(1, "No winner")
        lines.insert(88, "No winner")
    return lines


def dict_1(lines, winner_record):
    for line in lines:
        if line not in roster:
            roster[line] = lines.count(line)
    # print(roster)
    return roster


def dict_2(lines, index, winner_record):
    for line in lines:
        if index not in series_record:
            series_record[index] = line
            index += 1
    return series_record
    # print(series_record)


def output(winner_record, roster, series_record):
    for count in range(winner_record):
        winner = series_record.get("f{winner_record}")
        record = roster.get("f{winner}")
    return winner
    return record

    # print(lines)
    print(winner)
    print(record)
    main()