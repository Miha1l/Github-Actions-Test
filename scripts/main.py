import sys
import time


def main():
    data = sys.argv[1]
    date = time.strptime(data, '%Y-%m-%dT%H:%M:%SZ')
    print(f'Дата создания: {date.tm_year}-{date.tm_mon}-{date.tm_day}')
    print(f'Время создания: {date.tm_hour}-{date.tm_min}-{date.tm_sec}')
    return


if __name__=='__main__':
    main()