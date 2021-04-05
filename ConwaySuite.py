LINE_JUMP = "\n"
SPACE_SEPARATOR = " "
EMPTY_STRING = ""


class ConwaySuite:
    def draw(self, line, deep):
        return self.drawSourceLine(line) + self.drawSuite(line, deep, EMPTY_STRING)

    def drawSourceLine(self, line):
        return line + LINE_JUMP

    def drawSuite(self, line, deep, conwaySuite):
        if deep == 0:
            return conwaySuite
        nextLine = self.drawNextLine(line)
        return self.drawSuite(nextLine, deep - 1, self.accumulateNextLine(conwaySuite, nextLine))

    def accumulateNextLine(self, conwaySuite, nextLine):
        return self.prependSuite(conwaySuite) + nextLine

    def prependSuite(self, conwaySuite):
        if not conwaySuite:
            return conwaySuite
        return conwaySuite + LINE_JUMP

    def drawNextLine(self, line):
        compressedLine = self.removeLineSpaces(line)
        return self.drawLineChunks(compressedLine, EMPTY_STRING)

    def drawLineChunks(self, compressedLine, chunks):
        if not compressedLine:
            return chunks.strip()
        indexOfNextDistinctNumber = self.indexOfNextDistinctNumber(compressedLine, 0)
        return self.drawLineChunks(
            self.tail(compressedLine, indexOfNextDistinctNumber + 1),
            self.accumulateChunks(compressedLine, chunks, indexOfNextDistinctNumber) + SPACE_SEPARATOR)

    def accumulateChunks(self, compressedLine, chunks, indexOfNextDistinctNumber):
        return chunks + self.countConsecutiveLineNumbers(compressedLine[0:indexOfNextDistinctNumber + 1])

    def tail(self, compressedLine, index):
        return compressedLine[index:]

    def indexOfNextDistinctNumber(self, compressedLine, index):
        if self.hasOnlyOneNumber(compressedLine) or self.nextNumberDifferent(compressedLine):
            return index
        return self.indexOfNextDistinctNumber(self.tail(compressedLine, 1), index + 1)

    def hasOnlyOneNumber(self, compressedLine):
        return len(compressedLine) == 1

    def nextNumberDifferent(self, compressedLine):
        return compressedLine[0] != compressedLine[1]

    def removeLineSpaces(self, line):
        return line.replace(SPACE_SEPARATOR, EMPTY_STRING)

    def countConsecutiveLineNumbers(self, compressedLine):
        return f'{len(compressedLine)}{SPACE_SEPARATOR}{compressedLine[0]}'
