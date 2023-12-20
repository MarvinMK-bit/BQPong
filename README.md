# BQPong
Bitcoin Quantum Pong - Text version

The game is set in an apocalyptic dystopia. The internet has been destroyed by WW3, but Bitcoin is still a valuable digital currency that can be transmitted around the world.

The game has two players, Player 1 and Player 2. They are recruits in a guessing-pong game.
On Player 1's turn, Player 2 sends a Bitcoin key, one character at a time, to Player 1 using a Quantum OTP (One Time pad) with a random key of size N. Player 1 must correctly guess the random key (classical channels are all either fried or tapped) and decipher the message. The fewer tries used to do this, the better the score. This could be done using manual guesswork, brute-force on a laptop, or better yet, a quantum computer itself.

On Player 2's turn, Player 1 is the one sending the Bitcoin key.

The winner gets a job with the MENTATS corporation.
