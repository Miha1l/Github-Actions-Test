import sys
import time


def main():
    data = sys.argv[1]
    date = time.strptime(data, '%Y-%m-%dT%H:%M:%SZ')
    creation_date = time.strftime('%Y-%m-%d', date)
    creation_time = time.strftime('%H:%M:%S', date)
    print(f'Дата создания: {creation_date}')
    print(f'Время создания: {creation_time}')
    return


if __name__=='__main__':
    main()