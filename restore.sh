#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Loading user fixtures..."
python manage.py loaddata bpinfo/fixtures/users.json

echo "==> Loading bpinfo fixtures..."
python manage.py loaddata bpinfo/fixtures/snippets.json

echo "==> Loading blockproducers fixtures..."
python manage.py loaddata bpinfo/fixtures/blockproducers.json

echo "==> Done!"
