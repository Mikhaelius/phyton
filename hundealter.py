def alterR():
  try:
    eingabe = int(input("Gebe Köter alter an"))


    alter = ''

    if eingabe == 1:
      alter = 14
    if eingabe == 2:
      alter = 22
    if eingabe > 2:
      alter = 5 * eingabe + 22
    print(alter)
  except ValueError:
    print("Echtes Alter angeben.")

alterR()
# should work now
#hunde einschlaefern