def calculate_sleep_debt(planned, actual):
  # Write code below 💖
  # for each day, calculate how much sleep we missed (0 if we slept enough)
  daily_debt = [max(0, planned[i] - actual[i]) for i in range(len(planned))]
  # sum up all the daily debts and add 1
  total_debt = sum(daily_debt) + 1

  # now we track the longest streak of consecutive days with sleep debt
  longest_streak = 0
  current_streak = 0

  # for each day's debt
  for debt in daily_debt:
    # if there's debt, we extend the streak
    if debt > 0:
      current_streak += 1
      longest_streak = max(longest_streak, current_streak)
    # otherwise we reset the streak
    else:
      current_streak = 0

  # return the total debt and the longest streak
  return total_debt, longest_streak