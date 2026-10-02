from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).parents[1] / "app.py"


def test_new_game_resets_game_state():
    app = AppTest.from_file(str(APP_PATH), default_timeout=5).run()

    app.session_state["attempts"] = 8
    app.session_state["secret"] = 42
    app.session_state["score"] = 65
    app.session_state["status"] = "won"
    app.session_state["history"] = [17, 42]

    app.button[1].click().run()

    assert app.session_state["attempts"] == 0
    assert app.session_state["score"] == 0
    assert app.session_state["status"] == "playing"
    assert app.session_state["history"] == []
    assert 1 <= app.session_state["secret"] <= 100
