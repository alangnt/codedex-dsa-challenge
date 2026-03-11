def minimum_components(components):
  # Write code below 💖
  # start with just the empty sum
  found = {0: 0}  # sum -> fewest components to reach it
  for val in components:
    # copy so we don't modify while iterating
    snapshot = dict(found)
    for total, count in snapshot.items():
      new_total = total + val
      if new_total <= 42:
        if new_total not in found or count + 1 < found[new_total]:
          found[new_total] = count + 1
  return found.get(42, -1)