# This file holds the column names of the tables as List objects

Votes_colnames = [
    "Id",
    "PostId",
    "VoteTypeId",
    "CreationDate",
    "UserId",
    "BountyAmount",
]
Users_colnames = [
    "Id",
    "Reputation",
    "CreationDate",
    "DisplayName",
    "LastAccessDate",
    "WebsiteUrl",
    "Location",
    "AboutMe",
    "Views",
    "Upvotes",
    "DownVotes",
    "ProfileImageUrl",
    "AccountId",
]
PostHistory_colnames = [
    "Id",
    "PostHistoryTypeId",
    "PostId",
    "RevisionGUID",
    "CreationDate",
    "Comment",
    "UserId",
    "Text",
    "ContentLicense",
]
Tags_colnames = ["Id", "TagName", "Count", "ExcerptPostId", "WikiPostId"]
PostLinks_colnames = [
    "Id",
    "CreationDate",
    "PostId",
    "RelatedPostId",
    "LinkTypeId",
]
Posts_colnames = [
    "Id",
    "PostTypeId",
    "AcceptedAnswerId",
    "CreationDate",
    "Score",
    "ViewCount",
    "Body",
    "OwnerUserId",
    "LastEditorUserId",
    "LastEditDate",
    "LastActivityDate",
    "CommentCount",
    "ContentLicense",
]
Comments_colnames = [
    "Id",
    "PostId",
    "Score",
    "Text",
    "CreationDate",
    "UserId",
    "ContentLicense",
]

Badges_colnames = ["Id", "UserId", "Name", "Date", "Class", "TagBased"]
