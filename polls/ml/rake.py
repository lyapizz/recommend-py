import RAKE

rake = RAKE.Rake(RAKE.SmartStopList())

keywords = rake.run(
    "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world",
    minCharacters=1, maxWords=3, minFrequency=1)
result = str()
for keyword in keywords:
    result += keyword[0]
    result += ","

print(result)
