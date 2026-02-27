# engine.py
"""
The game module contains the function 'run_game' - the universal
game-running logic.

Its main features are:
- Accept a game module and a user's name as inputs.
- Print the game's instruction.
- Run a loop for a predefined number of rounds (e.g., 3).
- Ask the game module for a question and its correct answer,
in each round.
- Get the user's input, validate it for the game type, normalize it
if necessary and compare it to the correct answer.
- Print the appropriate feedback ("Correct!" or the error message) and
handle a wrong answer by ending the game.
- Print the congratulations message, if all rounds are passed.
"""


from brain_games.games.utils import get_user_answer, is_valid_answer, normalize_answer

ROUNDS_TO_WIN = 3


def run_game(game_module, user_name):
    """Run a game for ROUNDS_TO_WIN rounds.


        Args:
        game_module: A module containing:
            - INSTRUCTION (str): How to play the game
            - ANSWER_TYPE (str): 'numeric' or 'yesno'
            - generate_round(): Returns (question, correct_answer)
        user_name (str): The player's name for personalized messages

        Returns:
        None: The function prints results directly and exits
    """
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
            print(
                f"'{user_answer}' is wrong answer. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
