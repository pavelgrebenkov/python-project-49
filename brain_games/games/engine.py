# engine.py
from brain_games.games.utils import is_valid_answer, normalize_answer, get_user_answer


ROUNDS_TO_WIN = 3


def run_game(game_module, user_name):
    """Run a game for ROUNDS_TO_WIN rounds."""
    print(game_module.INSTRUCTION)

    correct_answers = 0
    while correct_answers < ROUNDS_TO_WIN:
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")

        user_answer = get_user_answer()

        # Validate based on game type
        if not is_valid_answer(user_answer, game_module.ANSWER_TYPE):
            print(f"Your answer isn't clear. Let's try again, {user_name}!")
            return

        # Normalize for comparison
        user_answer = normalize_answer(user_answer, game_module.ANSWER_TYPE)

        if user_answer == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
