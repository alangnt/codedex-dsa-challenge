def find_missing_colors(grid):
  # Write code below 💖
  # these are all the possible colors
  all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  # we create a set to store colors that are in the grid
  colors_in_grid = set()
  # for each row in the grid
  for row in grid:
    # for each cell in the row
    for cell in row:
      # we add the color to the set
      colors_in_grid.add(cell)
  # then we find all colors that are NOT in the grid
  missing = [color for color in all_colors if color not in colors_in_grid]
  # and return them
  return missing