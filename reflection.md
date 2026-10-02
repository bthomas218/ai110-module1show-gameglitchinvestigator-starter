# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

### Bugs I noticed

- The game does not reset properly when the new game button is clicked
- Hint always says go lower regardless of the value of the guess relative to the actual answer
- Changing difficulty mid-game does not reset the game state properly: only max attempts are reset,
  current attempts and the secret and history is not reset
- "Normal" difficulty has a higher number of attempts than "easy" but a larger range than "hard" (not sure if this is intended)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                        | Expected Behavior                                     | Actual Behavior                                                                                    | Console Output / Error                                                                                                                                                                                      |
| ---------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Guess 20 with secret 100     | Report "Too Low" and say "Go HIGHER!"                 | Reported "Too High" and said "Go HIGHER!" because the values were compared as strings              | `print(check_guess(20, "100"))` → `('Too High', '📈 Go HIGHER!')`                                                                                                                                           |
| Guess 120 with secret 100    | Report "Too High" and say "Go LOWER!"                 | Reported "Too High" but said "Go HIGHER!"                                                          | `print(check_guess(120, "100"))` → `('Too High', '📈 Go HIGHER!')`                                                                                                                                          |
| Click New Game after winning | Start with score 0, playing status, and empty history | Attempts and secret reset, but score stayed 65, status stayed `won`, and history stayed `[17, 42]` | `print(state)` before/after reset → `{'attempts': 8, 'secret': 42, 'score': 65, 'status': 'won', 'history': [17, 42]}` → `{'attempts': 0, 'secret': 73, 'score': 65, 'status': 'won', 'history': [17, 42]}` |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - GPT-5.6-Luna on Codex
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I accepted the AI's suggestion for fixing the new game handler clearing the score, returning the status to `playing`, and emptying the guess history in addition to resetting attempts and secret. I verified the result by running the game and confirming that all state variables were reset correctly using the developer debug info tab
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - When fixing the hint display, the AI suggested converting the secret to an integer before comparison, which resolved the string comparison issue, but it also made the hints inverted (e.g., "Go HIGHER!" when the guess was too low)

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - When the output for the given input matched expected behavior
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - For the initial hint fix I manually tested the fix by running the game with various inputs that were deliberately lower/higher relative to the secret and verifying that the hints were displayed correctly, this showed me that the hints were inverted.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit "reruns" occur when the app needs to update its display, often triggered by user interactions or changes in the session state. The "session state" is a dictionary that stores variables across these reruns, allowing the app to remember values between updates.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - A strategty that worked was keeping the AI focused on making the smallest changes necessary to fix the issues. This is made it easy to identify and fix the root causes of the problems, and verify the generated solution worked without affecting anything else.
- What is one thing you would do differently next time you work with AI on a coding task?
  - One thing I would do differently is to be more cautious about accepting AI suggestions without thoroughly testing them in the context of the entire application.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project made me realize that while AI can generate code quickly, it's crucial to understand the underlying logic and test thoroughly to ensure the code works as expected in all scenarios.
