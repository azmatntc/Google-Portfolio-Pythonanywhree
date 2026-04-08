#!/bin/bash

# 1. Build Frontend
echo "Building Svelte Frontend..."
npm run build

# 2. Sync Static Files to Django
echo "Syncing static files to Django..."
mkdir -p backend/static/frontend
cp -r dist/* backend/static/frontend/

# 3. Commit and Push
echo "Committing changes..."
git add .
git commit -m "Build: Production frontend update $(date)"
git push origin main

# 4. PythonAnywhere Reload (Optional via API)
# curl -X POST https://www.pythonanywhere.com/api/v0/user/$USER/webapps/$DOMAIN/reload/ \
#  -H "Authorization: Token $API_TOKEN"

echo "Deployment automation complete."
