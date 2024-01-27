from gendiff import generate_diff
import pytest
import os


@pytest.fixture
def fixtures_path():
    return os.path.join("tests", "fixtures")


def test_for_json(fixtures_path):
    first_file = os.path.join(fixtures_path, "file1.json")
    second_file = os.path.join(fixtures_path, "file2.json")
    answer = os.path.join(fixtures_path, 'answer.py')
    expected = open(answer, 'r')
    assert generate_diff(first_file, second_file) == expected.read()


def test_for_yaml(fixtures_path):
    first_file = os.path.join(fixtures_path, "file1.yaml")
    second_file = os.path.join(fixtures_path, "file2.yaml")
    answer = os.path.join(fixtures_path, 'answer.py')
    expected = open(answer, 'r')
    assert generate_diff(first_file, second_file) == expected.read()


def test_for_trees_json(fixtures_path):
    first_file = os.path.join(fixtures_path, "tree1.json")
    second_file = os.path.join(fixtures_path, "tree2.json")
    answer = os.path.join(fixtures_path, 'answer_trees.py')
    expected = open(answer, 'r')
    assert generate_diff(first_file, second_file) == expected.read()


def test_for_trees_yaml(fixtures_path):
    first_file = os.path.join(fixtures_path, "tree1.yaml")
    second_file = os.path.join(fixtures_path, "tree2.yaml")
    answer = os.path.join(fixtures_path, 'answer_trees.py')
    expected = open(answer, 'r')
    assert generate_diff(first_file, second_file) == expected.read()
