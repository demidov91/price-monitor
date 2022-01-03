import csv
import datetime
import os.path

from price_monitor.fetcher import query_data


def run():
    data = query_data()
    for item in data:
        item['datetime'] = item['datetime'].strftime('%Y-%m-%d %H:%M:%S')

    base_filename = datetime.date.today().strftime("%Y-%m-%d")
    filename = base_filename + '.csv'
    index = 1

    while os.path.exists(filename + '.csv'):
        index += 1
        filename = f'{base_filename}-{index}.csv'

    with open(filename, mode='wt', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['source', 'identifier', 'datetime', 'price'],
        )
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    run()
