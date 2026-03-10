def blood_moon(time):
  # Write code below 💖
  # first we split the time string into hours and minutes
  h, m = map(int, time.split(":"))
  # then we convert everything to total minutes
  total = h * 60 + m
  # the interval between each blood moon is 2h48 = 168 minutes
  interval = 2 * 60 + 48  # 168 minutes

  # we create a list to store the next 3 blood moon times
  result = []
  # for each of the 3 next blood moons
  for _ in range(3):
    # we add the interval and wrap around midnight
    total = (total + interval) % (24 * 60)
    # then we format it back to HH:MM and add it to the list
    result.append(f"{total // 60:02}:{total % 60:02}")

  # return the list of 3 upcoming blood moon times
  return result