import sys
import os

# Add the current directory to path
sys.path.append(os.getcwd())

from loguru import logger
from rag import initialize_components

print("--- STARTING DEBUG ---")
try:
    success = initialize_components()
    if success:
        print("--- SUCCESS ---")
    else:
        print("--- FAILURE: initialize_components returned False ---")
except Exception as e:
    print(f"--- FAILURE: Exception: {e} ---")
