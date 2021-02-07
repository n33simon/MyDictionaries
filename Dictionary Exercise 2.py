filename = "WorldSeriesWinners.txt"
roster = {}
series_record = {}
index = 1903


def main():
    # create lines
    lines = create_lines()

    # prompt user
    winner_record = int(
        input("What year would you like to know the World Series Winner (1903-2008?) ")
    )

    # create dictionary 1
    records = dict_1(lines)

    # create dictionary 2
    series = dict_2(lines, index)

    # get Series and Record finding
    output(winner_record)


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
    # print(roster)
    return roster


def dict_2(lines, index):
    for line in lines:
        if index not in series_record:
            series_record[index] = line
            index += 1
    # print(series_record)
    return series_record


def output(winner_record):
    for k in series_record:
        choice = series_record.__getitem__(int(winner_record))
        # print(choice)   <---prints out the team in correct format but too many times

    for v in roster:
        team = roster.__getitem__(str(choice))
        # print(team)   <--prints out the record too many times

    print(
        "The winning team was the:"
        + "\n"
        + choice
        + "A total amount of World Series wins:"
    )
    print(team)


main()
