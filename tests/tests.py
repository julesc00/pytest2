import pytest
import os
import shutil
import subprocess
from pathlib import Path


def test_list_empty_dir():
    """Test -ls in an empty folder, then rm dir."""
    fldr_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder"
    os.mkdir(fldr_path)
    result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)
    
    assert not result.stdout



def test_simple_ls():
    """Test -ls, with file exists."""
    file_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder/first.txt"
    Path(file_path).touch()
    result = subprocess.run(["ls", file_path], stdout=subprocess.PIPE)

    assert result.stdout
    
    fldr_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder"
    shutil.rmtree(fldr_path, ignore_errors=True)
