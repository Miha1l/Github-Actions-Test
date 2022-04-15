from datetime import datetime
import pytz


def main():
    # date_time_str = '${{github.event.pull_request.created_at}}'
    date_time_str = "2022-04-20T11:16:08Z"
    timezone = pytz.timezone("Etc/GMT-6")
    date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%SZ").astimezone(timezone)
    creation_date = str(date_time_obj.date())
    creation_time = str(date_time_obj.time())
    print(f"Дата создания: {creation_date}")
    print(f"Время создания: {creation_time}")
    return


if __name__=='__main__':
    main()