def wordle_guess(secret, guess):
  # Write code below 💖
  count = 0

  # for each character from secret and guess
  for i in range(5):
    # if they're the same, add 1
    if secret[i] == guess[i]:
      count += 1
  
  # return how many are correct
  return count