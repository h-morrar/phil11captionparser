def main():

    lectureNum = "1"

    originalFileName = "lecture-" + lectureNum
    originalFileObj = open(r"%s.txt" % originalFileName, "r")

    newFileName = originalFileName + "-parsed"
    newFileObj = open(r"%s.txt" % newFileName, "a")

    Lines = originalFileObj.readlines()

    for line in Lines:
        if (line[0].isdigit() and (line[1].isdigit()) and (line[2] == ":") and (line[3].isdigit()) and (line[4].isdigit())):
            continue
        elif (line.strip() == ""):
            continue
        else:
            newFileObj.write(line.strip() + " ")

main()
