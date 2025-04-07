#!/bin/sh
set -e

echo "⏳ Waiting for database at $DB_HOST:$DB_PORT..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "✅ Database is up. Running migrations..."
flask db upgrade

echo "🚀 Starting Flask app..."
exec "$@"
# This script waits for the database to be available before running migrations and starting the Flask app.
# It uses `nc` (netcat) to check if the database is reachable at the specified host and port.
# If the database is not reachable, it sleeps for 1 second and checks again.