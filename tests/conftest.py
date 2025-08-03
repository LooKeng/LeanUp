import tempfile
import pytest
from pathlib import Path
from leanup.const import LEANUP_CACHE_DIR


@pytest.fixture
def cache_dir():
    """Fixture to provide the LeanUp cache directory."""
    return LEANUP_CACHE_DIR

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)

@pytest.fixture
def mock_elan_home(temp_dir):
    """Create a mock elan home directory for testing"""
    elan_home = temp_dir / '.elan'
    elan_home.mkdir()
    (elan_home / 'bin').mkdir()
    return elan_home