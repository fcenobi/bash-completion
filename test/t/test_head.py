import pytest


class TestHead:
    @pytest.mark.complete(
        "head --",
        require_cmd=True,
        xfail=(
            "! head --help &>/dev/null || "
            "! head --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
