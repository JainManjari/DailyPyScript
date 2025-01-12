#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip3 --version')


# In[7]:


get_ipython().system('pip3 install gitpython --break-system-packages')


# In[64]:


import os
from git import Repo
import time


# In[65]:


# Set your repository path and file details
repo_path = "/Users/manjarijain/Desktop/Git/DailyPyScript"  # Path to your local Git repository
file_to_edit = "DailyUpdates.txt"  # File you want to edit
commit_message = getString("Update DailyUpdates.txt", epoch_time)


# In[66]:


github_remote_name = "origin"
branch_name = "main" 


# In[67]:


def getString(content, epoch_time):
    return (content+" at epoch {epoch}").format(epoch=epoch_time)


# In[68]:


def edit_file(file_path, content_to_add):
    try:
        with open(file_path, "w") as file:
            file.write(content_to_add)
        print(f"File '{file_path}' updated successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")


# In[69]:


def push_to_github(repo, commit_message):
    try:
        # Add changes to the staging area
        repo.git.add(update=True)

        # Commit the changes
        repo.index.commit(commit_message)
        print(f"Committed changes with message: '{commit_message}'")

        # Push changes to GitHub
        remote = repo.remote(name=github_remote_name)
        remote.push(branch_name)
        print(f"Changes pushed to GitHub on branch '{branch_name}'.")
    except Exception as e:
        print(f"Error pushing to GitHub: {e}")


# In[70]:


def main():
    # Initialize the repository
    try:
        epoch_time = int(time.time())
        repo = Repo(repo_path)
        if repo.bare:
            print("Repository not initialized. Please check the repository path.")
            return

        # Edit the file
        file_path = os.path.join(repo_path, file_to_edit)
        content_to_add = getString("\nNew content added via Python script", epoch_time)
        edit_file(file_path, content_to_add)

        # Push to github
        push_to_github(repo, commit_message)

    except Exception as e:
        print(f"Error with the repository: {e}")


# In[72]:


if __name__ == "__main__":
    main()


# In[ ]:




