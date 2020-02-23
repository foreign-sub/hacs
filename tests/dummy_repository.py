"""Create a dummy repository."""
# pylint: disable=missing-docstring
from homeassistant.core import HomeAssistant
from integrationhelper import Logger

from custom_components.hacs.helpers.install import version_to_install
from custom_components.hacs.repositories import HacsAppdaemon
from custom_components.hacs.repositories import HacsIntegration
from custom_components.hacs.repositories import HacsPlugin
from custom_components.hacs.repositories import HacsPythonScript
from custom_components.hacs.repositories import HacsTheme
from custom_components.hacs.repositories.repository import HacsRepository
from custom_components.hacs.repositories.repositorydata import RepositoryData
from tests.sample_data import repository_data


def dummy_repository_base(repository=None):
    if repository is None:
        repository = HacsRepository()
    repository.hacs.hass = HomeAssistant()
    repository.hacs.hass.data = {"custom_components": []}
    repository.logger = Logger("hacs.test.test")
    repository.information.full_name = "test/test"
    repository.versions.available = "3"
    repository.status.selected_tag = "3"
    repository.ref = version_to_install(repository)
    repository.manifest = {"config_flow": False, "domain": "test"}
    repository.releases.published_tags = ["1", "2", "3"]
    repository.data = RepositoryData().create_from_dict(repository_data)
    repository.data.name = "test"
    return repository


def dummy_repository_integration():
    repository = HacsIntegration("test/test")
    return dummy_repository_base(repository)


def dummy_repository_theme():
    repository = HacsTheme("test/test")
    return dummy_repository_base(repository)


def dummy_repository_plugin():
    repository = HacsPlugin("test/test")
    return dummy_repository_base(repository)


def dummy_repository_python_script():
    repository = HacsPythonScript("test/test")
    return dummy_repository_base(repository)


def dummy_repository_appdaemon():
    repository = HacsAppdaemon("test/test")
    return dummy_repository_base(repository)
