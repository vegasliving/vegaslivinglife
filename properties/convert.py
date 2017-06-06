from __future__ import unicode_literals
import csv
from django.conf import settings
settings.configure()

from pprint import pprint
from models import Listing, ListingManager

csvfile = 'listing.csv'

with open(csvfile) as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, map(str, row))) for row in reader]
    pprint(a[0:2])
    print(len(a))

