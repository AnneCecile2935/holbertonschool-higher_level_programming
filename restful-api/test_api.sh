#!/bin/bash

# Couleurs pour le terminal
GREEN="\e[32m"
RED="\e[31m"
NC="\e[0m"

echo -e "${GREEN}--- 1. /basic-protected sans identifiants ---${NC}"
curl -i http://localhost:5000/basic-protected

echo -e "\n${GREEN}--- 2. /basic-protected avec identifiants user1 ---${NC}"
curl -i -u user1:password http://localhost:5000/basic-protected

echo -e "\n${GREEN}--- 3. Login user1 (obtenir JWT) ---${NC}"
USER_TOKEN=$(curl -s -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password"}' | jq -r '.access_token')

echo -e "${GREEN}Token user1:${NC} $USER_TOKEN"

echo -e "\n${GREEN}--- 4. /jwt-protected avec token user1 ---${NC}"
curl -i http://localhost:5000/jwt-protected \
  -H "Authorization: Bearer $USER_TOKEN"

echo -e "\n${GREEN}--- 5. /admin-only avec token user1 (doit échouer) ---${NC}"
curl -i http://localhost:5000/admin-only \
  -H "Authorization: Bearer $USER_TOKEN"

echo -e "\n${GREEN}--- 6. Login admin1 (obtenir JWT) ---${NC}"
ADMIN_TOKEN=$(curl -s -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin1", "password": "password"}' | jq -r '.access_token')

echo -e "${GREEN}Token admin1:${NC} $ADMIN_TOKEN"

echo -e "\n${GREEN}--- 7. /admin-only avec token admin1 ---${NC}"
curl -i http://localhost:5000/admin-only \
  -H "Authorization: Bearer $ADMIN_TOKEN"

echo -e "\n${GREEN}--- Fin des tests ---${NC}"
