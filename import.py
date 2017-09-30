import os
from time import time

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SimpleMark.settings")
django.setup()


def main():
    file_path = './data/'
    all_files = os.listdir(file_path)
    data_list = []
    count = 0
    for file in all_files:
        with open('data/' + file, 'r', encoding='utf-8') as f:
            paragraph_id = file[:-4]
            paragraph = f.read()
            data_list.append(Paragraph(id=paragraph_id, paragraph=paragraph))

        count += 1
        if count % 10000 == 0:
            print('Done', count)
            Paragraph.objects.bulk_create(data_list)
            data_list = []

    print(count)
    Paragraph.objects.bulk_create(data_list)


if __name__ == "__main__":
    from pars.models import Paragraph
    start_time = time()
    main()
    end_time = time()
    print(str(end_time-start_time))
