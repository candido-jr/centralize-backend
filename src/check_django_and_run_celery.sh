#!/bin/bash

# 1. See the current path I'm in
current_path=$(pwd)
echo "Current path: $current_path"

# 2. Check if there is a Django project inside it
if [ -f "manage.py" ]; then
    echo "Django project found."

    # Infer the Django project name from manage.py
    project_name=$(grep -oP 'os\.environ\.setdefault\("DJANGO_SETTINGS_MODULE", "\K[^.]+' manage.py)
    
    if [ -z "$project_name" ]; then
        echo "Warning: Could not infer the Django project name."
    else
        echo "Django project name inferred: $project_name"
        
        # 4. If there is, it runs celery inside the project
        celery -A "$project_name" worker --loglevel=info
    fi
else
    # 3. If there isn't, it shows a warning
    echo "Warning: No Django project found in the current directory."
fi
