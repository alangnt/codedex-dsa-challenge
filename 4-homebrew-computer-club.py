def dompier_music(switches):
  # Write code below 💖
  # this maps each frequency to its musical note
  frequency_to_note = {
    261: "C4",
    294: "D4",
    329: "E4",
    349: "F4",
    392: "G4",
    440: "A4",
    494: "B4",
    523: "C5",
    0: "REST"
  }
  # we create a list to store the notes
  result = []
  # for each binary switch pattern
  for switch in switches:
    # we convert the binary string to a decimal number
    decimal = int(switch, 2)
    # then we look up the note for that frequency and add it
    result.append(frequency_to_note[decimal])
  # return the list of notes
  return result