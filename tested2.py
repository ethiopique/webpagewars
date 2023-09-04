import os
import subprocess
from datetime import datetime

# Replace these variables with your own values
repository_path = "/home/seilous/try/net/webpagewars"  # Local path to your friend's repository
files_directory = "/home/seilous/Files"  # Local path to the directory containing your 50 files
git_username = "Byronseilous"
git_email = "104057957+Byronseilous@users.noreply.github.com"

# Change directory to your repository
os.chdir(repository_path)

# Add, commit, and push each file individually
for file_name in os.listdir(files_directory):
    if os.path.isfile(os.path.join(files_directory, file_name)):
        # Calculate the commit date based on the file's modification time
        file_path = os.path.join(files_directory, file_name)
        commit_date = datetime.utcfromtimestamp(os.path.getmtime(file_path))
        commit_date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Add the file
        subprocess.run(["git", "add", file_name])

        # Commit with the commit date matching the file's modification time
        subprocess.run(
            ["git", "commit", "-m", f"Update {file_name}"],
            env={
                "GIT_COMMITTER_DATE": commit_date_str,
                "GIT_AUTHOR_NAME": git_username,
                "GIT_AUTHOR_EMAIL": git_email,
                "GIT_COMMITTER_NAME": git_username,
                "GIT_COMMITTER_EMAIL": git_email,
            },
        )

        # Push to the repository
        subprocess.run(["git", "push", "origin", "master"])
