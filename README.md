# Bluesky API Management
Set of scripts to use the Bluesky API (ATProto)

## Feature(s)
- Programatically add users to lists (convenient for mass blocking)

## Installation
- Install Python
- Use a virtual environment
- Install python libraries with `python -m pip install -r requirements.txt`

## Usage
- Add user to list: `python bluesky_addToList.py`
  The script will connect to the BlueSky API, look up user handle, return a DID identifier, then add DID to the list
  
