import pytest


class TestXvnc4viewer:

    @pytest.mark.complete("xvnc4viewer -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xvnc4viewer -PreferredEncoding ")
    def test_2(self, completion):
        assert completion.list == "hextile raw zrle".split()

    @pytest.mark.complete("xvnc4viewer --preferredencoding ")
    def test_3(self, completion):
        assert completion.list == "hextile raw zrle".split()
