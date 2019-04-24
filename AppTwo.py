# Waite Armstrong
# MIST 320 EC#1
t=open('2801-full.log')
badRootAttempts = 0
for line in t:
    if line.find("Failed password for root") != -1:
        badRootAttempts+=1
t.close()
print("There were XX " + str(badRootAttempts) + " amount of bad login attempts for the root user.")