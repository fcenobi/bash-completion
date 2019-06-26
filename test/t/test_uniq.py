import pytest


class TestUniq:
    @pytest.mark.complete(
        "uniq --",
        require_cmd=True,
        xfail=(
            "! uniq --help &>/dev/null || "
            "! uniq --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
