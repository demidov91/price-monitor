import csv
import datetime

from price_monitor.fetcher import query_data


def run():
    data = query_data()
    for item in data:
        item['datetime'] = item['datetime'].strftime('%Y-%m-%d %H:%M:%S')
    with open(f'{datetime.date.today().strftime("%Y-%m-%d")}.csv', mode='wt', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['source', 'identifier', 'datetime', 'price'],
        )
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    run()
