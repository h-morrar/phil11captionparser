def main():
    lectureNum = "1"
    originalFileName = "lecture-" + lectureNum
    originalFileObj = open(r"%s.txt" % originalFileName, "r")

    newFileName = originalFileName + "-parsed"
    newFileObj = open (r"%s.txt" % newFileName, "w")

main()
