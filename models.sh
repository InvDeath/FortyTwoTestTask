#!/bin/bash
python manage.py all_models | grep -v 'error' > $(date +"%m_%d_%Y").dat