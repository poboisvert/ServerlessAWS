import app


def test_get_quote():
    res = app.get_root()

    assert "message" in res
