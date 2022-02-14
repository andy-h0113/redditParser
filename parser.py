#! python3
import pandas as pd
import praw
import pandas
import datetime as dt
from praw.models import MoreComments
from comment import Comment

def parser():
    # Retrieving post thread and reddit API
    postUrl = "https://www.reddit.com/r/AskMen/comments/sc91a6/why_dontdo_you_wear_makeup/"

    reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', client_secret='SECRET_KEY_27_CHARS', user_agent='parser')

    submission = reddit.submission(url=postUrl)

    submission.comments.replace_more(limit=0)

    #this set will hold all the Comments(Class)
    commentCatalogue = set()

    # For loop only goes through Top Level Comments
    for top_level_comment in submission.comments:
        commentFiller = Comment(top_level_comment.author, top_level_comment.id, top_level_comment.body, top_level_comment.score, top_level_comment.created)
        commentCatalogue.add(commentFiller)

    # Loops through all submissions
    for comment in submission.comments.list():
        authorCheck = scan_comments(comment, commentCatalogue)
        if authorCheck:
            set_new_comment(comment, commentCatalogue)
        else:
            commentFiller = Comment(comment.author)
            commentFiller.setNewComment(comment.id, comment.body, comment.score)
            commentCatalogue.add(commentFiller)

    comments_dict = { "author" : [], "top_level_comment" : [], "top_level_score" : [], "created" : [], "replies" : []}

    for redditor in commentCatalogue:
        comments_dict["author"].append(redditor.getAuthor())
        comments_dict["top_level_comment"].append(redditor.getTopCommentText())
        comments_dict["top_level_score"].append(redditor.getTopCommentScore())
        comments_dict["created"].append(redditor.getTopDate())
        comments_dict["replies"].append(redditor.getReplies())

    comments_data = pd.DataFrame(comments_dict)
    _timestamp = comments_data["created"].apply(get_date)
    comments_data = comments_data.assign(timestamp = _timestamp)
    comments_data.to_csv('askMenPost.csv', index=False)



def get_date(created):
    return dt.datetime.fromtimestamp(created)

def scan_comments(commentInfo, commentCat):
    for i in commentCat:
        if str(commentInfo.author) == i.getAuthor():
            return True
    return False

def set_new_comment(commentInfo, commentCat):
    for x in commentCat:
        if str(commentInfo.author) == x.getAuthor() and commentInfo.id != x.getTopCommentCode():
            x.setNewComment(commentInfo.id, commentInfo.body, commentInfo.score)


def main():
    parser()
