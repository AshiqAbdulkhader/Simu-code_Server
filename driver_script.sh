#!/bin/bash
gnome-terminal -- uvicorn Server:app --reload & gnome-terminal -- "./localtunnel.sh"
