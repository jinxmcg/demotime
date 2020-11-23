#!/bin/bash
set -Eeuo pipefail

echo "=> Creating an user in MongoDB"
mongo $MONGO_INITDB_DATABASE --eval "db.dropUser('$MONGO_INITDB_USERNAME');"
mongo $MONGO_INITDB_DATABASE --eval "db.createUser({user: '$MONGO_INITDB_USERNAME', pwd: '$MONGO_INITDB_PASSWORD', roles: [ 'readWrite' ]});"