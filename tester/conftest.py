import json

import pytest
import yaml


def pytest_addoption(parser):
    parser.addoption("--actual_file_path", action="store", default="./data/actual1.json")
    parser.addoption("--config_file_path", action="store", default="./data/config1.yml")


@pytest.fixture(scope="session")
def actual_file_path(request):
    return request.config.option.actual_file_path


@pytest.fixture(scope="session")
def config_file_path(request):
    return request.config.option.config_file_path


@pytest.fixture(scope="module")
def load_actual_and_conf(request):
    with open(request.config.option.actual_file_path, 'rb') as actual:
        pytest.actual_dict = json.load(actual)

    with open(request.config.option.config_file_path, 'rb') as conf:
        pytest.conf_dict = yaml.safe_load(conf.read())
