import unittest
from unittest.mock import patch, MagicMock
import io
import time

# Import the functions from the number_guessing_game.py module
# Assume your game script is named number_guessing_game.py
# If it's named differently, replace it accordingly.
import number_guessing_game

class TestNumberGuessingGame(unittest.TestCase):
    
    @patch('number_guessing_game.input')
    @patch('number_guessing_game.random.randint')
    @patch('number_guessing_game.time.time')
    def test_easy_difficulty(self, mock_time, mock_randint, mock_input):
        # Set up mocks
        mock_input.side_effect = ['1', '50', '30']
        mock_randint.return_value = 30
        mock_time.side_effect = [0, 1]  # Simulate 1 second elapsed
        
        # Run the game function
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            number_guessing_game.play_game()
            output = fake_out.getvalue()

        # Check for expected output
        self.assertIn("Congratulations! You guessed the correct number", output)
        self.assertIn("Time taken: 1.00 seconds.", output)

    @patch('number_guessing_game.input')
    @patch('number_guessing_game.random.randint')
    @patch('number_guessing_game.time.time')
    def test_medium_difficulty_incorrect_guess(self, mock_time, mock_randint, mock_input):
        # Set up mocks
        mock_input.side_effect = ['2', '50', '40', '30']
        mock_randint.return_value = 35
        mock_time.side_effect = [0, 1, 2]  # Simulate 2 seconds elapsed
        
        # Run the game function
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            number_guessing_game.play_game()
            output = fake_out.getvalue()

        # Check for expected output
        self.assertIn("Incorrect! The number is greater than 50", output)
        self.assertIn("Incorrect! The number is less than 40", output)
        self.assertIn("Congratulations! You guessed the correct number", output)
        self.assertIn("Time taken: 2.00 seconds.", output)

    @patch('number_guessing_game.input')
    @patch('number_guessing_game.random.randint')
    def test_high_score_tracking(self, mock_randint, mock_input):
        # Set up mocks
        mock_input.side_effect = ['2', '50', '30', '40', '20']
        mock_randint.return_value = 25
        
        # Run the game function twice to test high score update
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            number_guessing_game.main()
            output_first_game = fake_out.getvalue()
        
        mock_input.side_effect = ['2', '20', '30']
        mock_randint.return_value = 25
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            number_guessing_game.main()
            output_second_game = fake_out.getvalue()

        # Check if high score is updated
        self.assertIn("New high score for Medium difficulty!", output_second_game)
        self.assertIn("Current High Scores:", output_second_game)
        self.assertIn("Medium: 3 attempts", output_second_game)

if __name__ == '__main__':
    unittest.main()
