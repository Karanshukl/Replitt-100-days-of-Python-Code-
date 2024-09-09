import csv, os

with open("100MostStreamedSongs.csv") as f:
  read = csv.DictReader(f)
  
  for row in read:
    new_dir = os.listdir()
    New_artist = row["Artist(s)"]
    print(New_artist)
    if New_artist not in new_dir:
      os.mkdir(New_artist)
    song = row["Song"]  
    print(row["Song"])
    path = os.path.join(f"{New_artist}/", song)
    with open(path, "w") as f:
      f.write(path)


