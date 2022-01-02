import pytest
import os
import shutil
import subprocess
from pathlib import Path


def test_list_empty_dir():
    """Test -ls in an empty folder, then rm dir."""
    fldr_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder"
    try:
        os.mkdir(fldr_path)
        result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)

        assert not result.stdout, "Listing an empty folder did not return expected results."
    finally:
        shutil.rmtree(fldr_path)


def test_simple_ls():
    """Test -ls, with file exists."""
    fldr_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder"
    try:
        file_path = "/Users/julio_briones/Documents/Dev/Python/Core/pytest2/test_folder/first.txt"
        os.mkdir(fldr_path)
        Path(file_path).touch()
        result = subprocess.run(["ls", file_path], stdout=subprocess.PIPE)
        print(f"Result: [{result}]")

        assert "first.txt" in str(result.stdout), "Listing a dir with one file didn't return expected results."
    finally:
        shutil.rmtree(fldr_path, ignore_errors=True)
