#!/bin/bash
prometheus-node-exporter &
python /app/main.py
