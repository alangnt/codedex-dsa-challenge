def calculate_score(elements):
  # Write code below 💖
  # tes will hold the total element score
  tes = 0
  # for each element: its name, base value, and list of GOE scores
  for name, base, goes in elements:
    # we sort the GOE scores from lowest to highest
    sorted_goes = sorted(goes)
    # drop the lowest and highest scores
    trimmed_goes = sorted_goes[1:-1]
    # then we calculate the average of the remaining scores
    average_goes = sum(trimmed_goes) / len(trimmed_goes)
    # and add the base value + the weighted average to the total
    tes += base + (average_goes * 0.1 * base)
  # return the total score rounded to 1 decimal
  return round(tes, 1)