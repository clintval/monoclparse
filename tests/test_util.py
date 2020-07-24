import pytest

from monoclparse.util import format_column_name


class TestUtil(object):
    """Unit tests for ``monoclparse.util``."""

    def test_format_column_name_squashes_first_two_levels(self):
        levels = ['prefix', 'suffix']
        assert format_column_name(levels) == 'prefix suffix'

    def test_format_column_name_ignores_extra_levels(self):
        levels = ['prefix', 'suffix', 'extra']
        assert format_column_name(levels) == 'prefix suffix'

    def test_format_column_name_replaces_unnamed_suffix(self):
        levels = ['prefix', 'Unnamed']
        assert format_column_name(levels) == 'prefix'

    def test_format_column_name_replaces_newlines(self):
        levels = ['prefix\nprefix', 'suffix\nsuffix']
        assert format_column_name(levels) == 'prefix prefix suffix suffix'
