import sys
import argparse


def calculate(year, month, day):
    import calendar
    try:
        result_day = calendar.weekday(year=year, month=month, day=day)
    except ValueError:
        return None
    return result_day


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',
                        type=int,
                        required=True,
                        help='Year')
    parser.add_argument('--month',
                        type=int,
                        required=True,
                        help='Month')
    parser.add_argument('--day',
                        type=int,
                        required=True,
                        help='Day')

    parsed_args = parser.parse_args(args)
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    if weekday is None:
        return 1
    print("Weekday {}".format(weekday))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
