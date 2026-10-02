# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose. This Streamlit game challenges the player to guess a hidden number, provides higher/lower hints, tracks attempts and score, and lets the player start a new round.
- [x] Detail which bugs you found. The hint logic compared numeric guesses with text secrets, the higher/lower messages were inverted, and the New Game button left score, status, and guess history from the previous round.
- [x] Explain what fixes you applied. We reproduced the bugs with printed console output, normalized secret values before comparison, corrected the hint messages, reset all game session state, and added collaboration comments near the fixes. We also moved the game helpers into `logic_utils.py`, added a Streamlit `AppTest` regression test for New Game, documented the findings in `reflection.md`, and verified the full suite with `4 passed`.

## 📸 Demo Walkthrough

This textual walkthrough demonstrates the repaired game from start to finish:

1. Start a Normal difficulty game. The Developer Debug Info shows a secret of `50`, with the score at `0`, status `playing`, and an empty guess history.
2. Enter `60` and submit it. The game reports `Too High` and displays `Go LOWER!`, confirming that a guess above the secret gives the correct directional hint.
3. Enter `40` and submit it. The game reports `Too Low` and displays `Go HIGHER!`, confirming that a guess below the secret gives the correct directional hint.
4. Enter `50` and submit it. The game reports `Win`, awards points, and changes the status to `won`. The comparison still works when the app passes the secret as text on an alternating attempt because the logic converts it to a number first.
5. Click **New Game**. The app generates a new secret and resets attempts, score, status, and guess history so the next round starts cleanly.

## 🧪 Test Results

```
uv run pytest
=============================================== test session starts ================================================
platform linux -- Python 3.13.11, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/brady/workspace/github.com/bthomas218/ai110-module1show-gameglitchinvestigator-starter
configfile: pyproject.toml
plugins: anyio-4.15.1
collected 4 items

tests/test_app.py .                                                                                          [ 25%]
tests/test_game_logic.py ...                                                                                 [100%]

================================================ 4 passed in 0.54s =================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
