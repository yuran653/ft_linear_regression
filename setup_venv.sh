#!/bin/bash

YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "${YELLOW}Creating Python virtual environment 'lg_venv'...${NC}"
python3 -m venv lg_venv
echo "${GREEN}'lg_venv' has been created successfully${NC}"

echo "${YELLOW}Activating the virtual environment...${NC}"
source lg_venv/bin/activate
echo "${GREEN}Virtual environment has been activated successfully${NC}"

echo "${YELLOW}Updating pip...${NC}"
pip install --upgrade pip
echo "${GREEN}'pip' has been updated successfully${NC}"

echo "${YELLOW}Installing required Python packages...${NC}"
pip install -r requirements.txt
echo "${GREEN}All required packages have been installed${NC}"

echo "${GREEN}Virtual environment setup is completed${NC}"
