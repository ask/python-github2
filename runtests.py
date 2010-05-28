#!/usr/bin/env python
"""Run all unit tests for this project"""

import sys
import os

# Add this to the path so we can "import github2"
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

import unittest
from tests import *

if __name__ == "__main__":
    unittest.main()
