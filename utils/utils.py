import os

import django

from pars.models import Paragraph

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SimpleMark.settings")
django.setup()


def main():
    f = open('results.txt')
    for line in f:
        Paragraph.objects.create(paragraph=line)
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')