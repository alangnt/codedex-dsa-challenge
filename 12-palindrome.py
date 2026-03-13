def check_palindrome(sequence):
  # Write code below 💖
  # ignore space and capitalization
  cleaned = sequence.replace(" ", "").lower()

  if cleaned[::-1] == cleaned:
    return True
  
  return False