#!/bin/bash
echo "Running formatting check..."
black --check .

echo "Running unit tests..."
PYTHONPATH=src pytest
