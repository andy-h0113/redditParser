class Comment:
    def __init__(self, author, commentCode = None, commentText = None, commentScore = None, commentDate = None):
        self._author = str(author) #string
        self._topLevel = [str(commentText), str(commentScore), commentDate, str(commentCode)]
        self._commentDict = dict()
    # def __init__(self, author, commentCode, commentText, commentScore):
    #     self._author = str(author)
    #     self._topLevel = []
    #     self._commentDict = {commentCode : [commentText, commentScore]}
    def getAuthor(self):
        return self._author
    def getTopCommentText(self):
        return self._topLevel[0]
    def getTopCommentScore(self):
        return self._topLevel[1]
    def getTopDate(self):
        return int(0 if self._topLevel[2] is None else self._topLevel[2])
    def getTopCommentCode(self):
        return self._topLevel[3]

    def getCommentText(self, code):
        return self._commentDict[code][0]
    def getCommentScore(self, code):
        return self._commentDict[code][1]
    def getReplies(self):
        return self._commentDict

    def setNewComment(self, newCode, newText, newScore):
        self._commentDict[newCode] = [newText, newScore]

    def __repr__(self):
        count = 0
        for i in self._commentDict:
            count += 1
        return "Author: " + self._author + " | Number of Comments: " + str(count) + " | TLC Code: " + self._topLevel[3]
