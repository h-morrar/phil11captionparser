import sys
# Usage: python3 parser.py lectureNumber inputFileName
def main():

    lectureNum = str(sys.argv[1])

    originalFileName = str(sys.argv[2])
    originalFileObj = open(r"%s.txt" % originalFileName, "r")

    newFileName = originalFileName + "-parsed.txt"
    newFileObj = open(r"%s" % newFileName, "a")

    Lines = originalFileObj.readlines()

    for line in Lines:
        if (line[0].isdigit() and (line[1].isdigit()) and (line[2] == ":") and (line[3].isdigit()) and (line[4].isdigit())):
            continue
        elif (line.strip() == ""):
            continue
        else:
            newFileObj.write(line.strip() + " ")

    originalFileObj.close()
    newFileObj.close()
main()
