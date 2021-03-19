import xml.etree.ElementTree as ET

# importing ElementTree to parse the xml file and read it's tags

import pandas as pd

import ntpath

# this modue returns name of a file given the path

import numpy as np

# filling the empty values of the pandas data frame with np.nan

from .columns import *

# Getting the column names of the tables

from tqdm.notebook import tqdm

# module to output progressbar in notebook

# Thiipt convert xml fileo pandaaframes
def convert_to_pd(path):
    table = ntpath.basename(path)
    data_list = []
    # getting the name of the xml file to see which table we're dealing with
    if table == "Votes.xml":
        dataframe = pd.DataFrame(columns=Votes_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        # Getting the root element of the xml file to iterate over all of it's
        # rows
                
        for row in tqdm(root, desc="Parsing Votes"):
            # Fetching all of the values in the row
            # The reason '.get()' is used is because it does not throw an
            # exception when it doesn't find the value of a given column, it
            # is also faster than using '.find()' with O(1) time complexity
            Id = row.attrib.get("Id")
            PostId = row.attrib.get("PostId")
            VoteTypeId = row.attrib.get("VoteTypeId")
            CreationDate = row.attrib.get("CreationDate")
            UserId = row.attrib.get("UserId")
            BountyAmount = row.attrib.get("BountyAmount")

            # This is the most optimal approach I have found to load the data
            # of every row using a dictionary rather than creating a
            # series appeding it to the dataframe every iteration
            data_list.append(
                {
                    "Id": Id,
                    "PostId": PostId,
                    "VoteTypeId": VoteTypeId,
                    "CreationDate": CreationDate,
                    "UserId": UserId,
                    "BountyAmount": BountyAmount,
                }
            )

        # Appending the list of dictionaries to the dataframe and filling None
        # values as np.nan
        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)
        return dataframe

    if table == "Users.xml":
        dataframe = pd.DataFrame(columns=Users_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing Users"):
            Id = row.attrib.get("Id")
            Reputation = row.attrib.get("Reputation")
            CreationDate = row.attrib.get("CreationDate")
            DisplayName = row.attrib.get("DisplayName")
            LastAccessDate = row.attrib.get("LastAccessDate")
            WebsiteUrl = row.attrib.get("WebsiteUrl")
            Location = row.attrib.get("Location")
            AboutMe = row.attrib.get("AboutMe")
            Views = row.attrib.get("Views")
            Upvotes = row.attrib.get("Upvotes")
            DownVotes = row.attrib.get("DownVotes")
            ProfileImageUrl = row.attrib.get("ProfileImageUrl")
            AccountId = row.attrib.get("AccountId")

            data_list.append(
                {
                    "Id": Id,
                    "Reputation": Reputation,
                    "CreationDate": CreationDate,
                    "DisplayName": DisplayName,
                    "LastAccessDate": LastAccessDate,
                    "WebsiteUrl": WebsiteUrl,
                    "Location": Location,
                    "AboutMe": AboutMe,
                    "Views": Views,
                    "Upvotes": Upvotes,
                    "DownVotes": DownVotes,
                    "ProfileImageUrl": ProfileImageUrl,
                    "AccountId": AccountId,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)
        return dataframe

    if table == "PostHistory.xml":
        dataframe = pd.DataFrame(columns=PostHistory_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing PostHistory"):
            Id = row.attrib.get("Id")
            PostHistoryTypeId = row.attrib.get("PostHistoryTypeId")
            PostId = row.attrib.get("PostId")
            RevisionGUID = row.attrib.get("RevisionGUID")
            CreationDate = row.attrib.get("CreationDate")
            Comment = row.attrib.get("Comment")
            UserId = row.attrib.get("UserId")
            Text = row.attrib.get("Text")
            ContentLicense = row.attrib.get("ContentLicense")

            data_list.append(
                {
                    "Id": Id,
                    "PostHistoryTypeId": PostHistoryTypeId,
                    "PostId": PostId,
                    "RevisionGUID": RevisionGUID,
                    "CreationDate": CreationDate,
                    "Comment": Comment,
                    "UserId": UserId,
                    "Text": Text,
                    "ContentLicense": ContentLicense,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)
        return dataframe

    if table == "PostLinks.xml":
        dataframe = pd.DataFrame(columns=PostLinks_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing PostLinks"):
            Id = row.attrib.get("Id")
            PostId = row.attrib.get("PostId")
            CreationDate = row.attrib.get("CreationDate")
            RelatedPostId = row.attrib.get("RelatedPostId")
            LinkTypeId = row.attrib.get("LinkTypeId")

            data_list.append(
                {
                    "Id": Id,
                    "CreationDate": CreationDate,
                    "PostId": PostId,
                    "RelatedPostId": RelatedPostId,
                    "LinkTypeId": LinkTypeId,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)

        return dataframe

    if table == "Posts.xml":
        dataframe = pd.DataFrame(columns=Posts_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing Posts"):
            Id = row.attrib.get("Id")
            PostTypeId = row.attrib.get("PostTypeId")
            AcceptedAnswerId = row.attrib.get("AcceptedAnswerId")
            CreationDate = row.attrib.get("CreationDate")
            Score = row.attrib.get("Score")
            ViewCount = row.attrib.get("ViewCount")
            Body = row.attrib.get("Body")
            OwnerUserId = row.attrib.get("OwnerUserId")
            LastEditorUserId = row.attrib.get("LastEditorUserId")
            LastEditDate = row.attrib.get("LastEditDate")
            LastActivityDate = row.attrib.get("LastActivityDate")
            CommentCount = row.attrib.get("CommentCount")
            ContentLicense = row.attrib.get("ContentLicense")

            data_list.append(
                {
                    "Id": Id,
                    "PostTypeId": PostTypeId,
                    "AcceptedAnswerId": AcceptedAnswerId,
                    "CreationDate": CreationDate,
                    "Score": Score,
                    "ViewCount": ViewCount,
                    "Body": Body,
                    "OwnerUserId": OwnerUserId,
                    "LastEditorUserId": LastEditorUserId,
                    "LastEditDate": LastEditDate,
                    "LastActivityDate": LastActivityDate,
                    "CommentCount": CommentCount,
                    "ContentLicense": ContentLicense,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)

        return dataframe

    if table == "Tags.xml":
        dataframe = pd.DataFrame(columns=Tags_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing Tags"):
            Id = row.attrib.get("Id")
            TagName = row.attrib.get("TagName")
            Count = row.attrib.get("Count")
            ExcerptPostId = row.attrib.get("ExcerptPostId")
            WikiPostId = row.attrib.get("WikiPostId")

            data_list.append(
                {
                    "Id": Id,
                    "TagName": TagName,
                    "Count": Count,
                    "ExcerptPostId": ExcerptPostId,
                    "WikiPostId": WikiPostId,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)

        return dataframe

    if table == "Comments.xml":
        dataframe = pd.DataFrame(columns=Comments_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing Comments"):
            Id = row.attrib.get("Id")
            PostId = row.attrib.get("PostId")
            Score = row.attrib.get("Score")
            CreationDate = row.attrib.get("CreationDate")
            Text = row.attrib.get("Text")
            UserId = row.attrib.get("UserId")
            ContentLicense = row.attrib.get("ContentLicense")

            data_list.append(
                {
                    "Id": Id,
                    "PostId": PostId,
                    "Score": Score,
                    "CreationDate": CreationDate,
                    "Text": Text,
                    "UserId": UserId,
                    "ContentLicense": ContentLicense,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)

        return dataframe

    if table == "Badges.xml":
        dataframe = pd.DataFrame(columns=Badges_colnames)
        tree = ET.parse(path)
        root = tree.getroot()
        
        for row in tqdm(root, desc="Parsing Badges"):
            Id = row.attrib.get("Id")
            UserId = row.attrib.get("UserId")
            Name = row.attrib.get("Name")
            Date = row.attrib.get("Date")
            Class = row.attrib.get("Class")
            TagBased = row.attrib.get("TagBased")

            data_list.append(
                {
                    "Id": Id,
                    "UserId": UserId,
                    "Name": Name,
                    "Date": Date,
                    "Class": Class,
                    "TagBased": TagBased,
                }
            )

        dataframe = pd.DataFrame(data_list).fillna(value=np.nan)

        return dataframe
