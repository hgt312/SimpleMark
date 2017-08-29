import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SimpleMark.settings")
django.setup()


from pars.models import Paragraph



def main():
    f = open('results.txt')
    for line in f:
        Paragraph.objects.create(paragraph=line)
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')
