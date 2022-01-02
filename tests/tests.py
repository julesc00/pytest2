import pytest
import os
import shutil
import subprocess
from pathlib import Path


class ListingTest(object):

    @staticmethod
    def test_list_empty_dir():
        """Test -ls in an empty folder, then rm dir."""
        fldr_path = "/tmp/test_folder"
        try:
            os.mkdir(fldr_path)
            result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)

            assert not result.stdout, "Listing an empty folder did not return expected results."
        finally:
            shutil.rmtree(fldr_path)

    @staticmethod
    def test_simple_ls():
        """Test -ls, with file exists."""
        fldr_path = "/tmp/test_folder"
        try:
            file1 = "/first.txt"
            os.mkdir(fldr_path)
            Path(fldr_path + file1).touch()
            result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)
            print(f"Result: [{result}]")

            assert "first.txt" in str(result.stdout), "Listing a dir with one file didn't return expected results."
        finally:
            shutil.rmtree(fldr_path, ignore_errors=True)

    @staticmethod
    def test_ls_multiple_files():
        """Test ls with multiple files exists."""
        fldr_path = "/tmp/test_folder"
        try:
            file1 = "/first.txt"
            file2 = "/second.doc"
            os.mkdir(fldr_path)
            Path(fldr_path + file1).touch()
            Path(fldr_path + file2).touch()
            result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)
            print(f"Result: [{result}]")

            assert "first.txt" in str(result.stdout), "Listing a dir multiple files didn't return expected results."
            assert "second.doc" in str(result.stdout), "Listing a dir multiple files didn't return expected results."
        finally:
            shutil.rmtree(fldr_path, ignore_errors=True)

    @staticmethod
    def test_not_ls_a_hidden_file():
        """Test not listing for a hidden file."""
        fldr_path = "/tmp/test_folder"
        try:
            file1 = "/first.txt"
            hidden_file = "/.hidden.txt"
            os.mkdir(fldr_path)
            Path(fldr_path + file1).touch()
            Path(fldr_path + hidden_file).touch()
            result = subprocess.run(["ls", fldr_path], stdout=subprocess.PIPE)
            print(f"Result: [{result}]")

            assert "first.txt" in str(result.stdout), "Listing a dir with one file didn't return expected results."
            # I guess hidden files do not show in .stdout, since test passes this way.
            assert ".hidden.txt" not in str(result.stdout), "ls a hidden file when it shouldn't have any."
        finally:
            shutil.rmtree(fldr_path, ignore_errors=True)

    @staticmethod
    def test_ls_a_hidden_file():
        """Test listing for a hidden file."""
        fldr_path = "/tmp/test_folder"
        try:
            file1 = "/first.txt"
            hidden_file = "/.hidden.txt"
            os.mkdir(fldr_path)
            Path(fldr_path + file1).touch()
            Path(fldr_path + hidden_file).touch()
            result = subprocess.run(["ls", "-a", fldr_path], stdout=subprocess.PIPE)
            print(f"Result: [{result}]")

            assert "first.txt" in str(result.stdout), "Listing a dir with one file didn't return expected results."
            # I guess hidden files do not show in .stdout, since test passes this way.
            assert ".hidden.txt" in str(result.stdout), "ls a hidden file when it shouldn't have any."
        finally:
            shutil.rmtree(fldr_path, ignore_errors=True)
