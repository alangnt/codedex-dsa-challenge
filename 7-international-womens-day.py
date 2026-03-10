def analyze(percentages):
  # Write code below 💖
  n = len(percentages)
  # calculate the net change per year
  # by dividing the total change by the number of intervals
  net_change = (percentages[-1] - percentages[0]) / (n - 1)
  net_change = round(net_change, 4)
  # to determine the trend, we compare the first 3-year avg vs the last 3-year avg
  first_avg = sum(percentages[:3]) / 3
  last_avg = sum(percentages[-3:]) / 3
  # if the last avg is higher, it's improving
  if last_avg > first_avg:
    trend = "improving"
  # if they're equal, it's stagnating
  elif last_avg == first_avg:
    trend = "stagnating"
  # otherwise it's declining
  else:
    trend = "declining"
  # count the number of dips (year-over-year decreases)
  dips = sum(1 for i in range(1, n) if percentages[i] < percentages[i - 1])
  # return the net change, trend, and number of dips
  return net_change, trend, dips