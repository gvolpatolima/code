import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

# Define the RPS moves as integers
moves = {"R": 0, "P": 1, "S": 2}

def player(prev_play, opponent_history=[]):
    """
    RPS player function that uses LSTM model to predict the next move.

    Args:
        prev_play (str): Previous play by the player, one of "R", "P", or "S".
        opponent_history (list): Opponent's move history, optional.

    Returns:
        next_move (str): Next move predicted by the LSTM model, one of "R", "P", or "S".
    """
    # If opponent_history is not provided, initialize an empty list
    if not opponent_history:
        opponent_history = []

    # Add the previous play to opponent_history
    opponent_history.append(prev_play)

    # Generate the corresponding player and opponent moves
    player_moves = opponent_history[:-1]
    opponent_moves = opponent_history[1:]

    # Convert the moves into integers
    player_moves_int = np.array([moves[move] for move in player_moves])
    opponent_moves_int = np.array([moves[move] for move in opponent_moves])

    # One-hot encode the moves
    player_moves_encoded = to_categorical(player_moves_int, num_classes=len(moves))
    opponent_moves_encoded = to_categorical(opponent_moves_int, num_classes=len(moves))

    # Create an LSTM model
    model = Sequential()
    model.add(LSTM(64, input_shape=(1, len(moves)), activation='relu'))
    model.add(Dense(len(moves), activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Reshape the input data for LSTM
    player_moves_encoded = player_moves_encoded.reshape(-1, 1, len(moves))

    # Train the LSTM model
    model.fit(player_moves_encoded, opponent_moves_encoded, epochs=50, batch_size=32, verbose=0)

    # Use the trained LSTM model to generate predictions
    test_player_move_int = moves[prev_play]
    test_player_move_encoded = to_categorical(test_player_move_int, num_classes=len(moves)).reshape(-1, 1, len(moves))
    predicted_opponent_move_encoded = model.predict(test_player_move_encoded)
    predicted_opponent_move_int = np.argmax(predicted_opponent_move_encoded)
    next_move = list(moves.keys())[predicted_opponent_move_int]

    return next_move

