import copy
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Add the src directory to the import path so tests can import the app module.
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from app import app, activities

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    original_state = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
