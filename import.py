import os
from time import time

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SimpleMark.settings")
django.setup()


from pars.models import Paragraph


def main():
    list = []
    f = open('results.txt')
    for line in f:
        paragraph_id, paragraph = line.split(' ')
        list.append(Paragraph(id=paragraph_id, paragraph=paragraph))
    f.close()
    Paragraph.objects.bulk_create(list)


if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    print(str(end_time-start_time))
