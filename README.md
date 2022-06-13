## Description

Api utilisant DnajgoRest Framework.

Backend de TFE.

## Installation

## Running

```bash
python manage.py runserver
```

## Export/Import database
```bash
python manage.py dumpdata -e contenttypes --indent 2 > dump.json
python manage.py loaddata dump_db.json
```

## Author

- Alloin Clément
