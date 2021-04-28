fp = open("bizimdata.txt", "a", encoding="utf8")

fp.write("Bu benim ilk satırım.\n")

fp.seek(0) # yine dosyanın başına git

fp.write("Kimler geldi kimler geçti.\n")
fp.close()
