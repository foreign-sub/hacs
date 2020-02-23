"""Test globals."""
# pylint: disable=missing-docstring
from custom_components.hacs.globals import get_hacs
from custom_components.hacs.globals import get_removed
from custom_components.hacs.globals import is_removed
from custom_components.hacs.globals import removed_repositories


def test_global_hacs():
    hacs = get_hacs()
    assert hacs.system.lovelace_mode == "storage"
    hacs.system.lovelace_mode = "yaml"
    hacs = get_hacs()
    assert hacs.system.lovelace_mode == "yaml"


def test_is_removed():
    repo = "test/test"
    assert not is_removed(repo)


def test_get_removed():
    repo = "removed/removed"
    removed = get_removed(repo)
    assert removed.repository == repo
