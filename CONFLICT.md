# Merge Conflict Report

## What Happened?

I created a branch named `experiment/tone` and changed the Persian greeting in `echo_lite.py` to a more formal response.

Then I switched to `main` and changed the same line to a more friendly response.

When I ran `git merge experiment/tone`, Git could not automatically merge the different changes and reported a conflict in `echo_lite.py`.

## How I Resolved It

1. I opened `echo_lite.py` and checked the conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`).
2. I compared the changes from both branches.
3. I chose a response that was both friendly and polite.
4. I removed the conflict markers.
5. I updated the greeting unit test to match the final response.
6. I ran the tests and staged the resolved files.
7. I completed the merge with a new Merge Commit.

## What I Learned

I learned that a merge conflict happens when Git cannot safely combine changes from different branches.

I also learned that I should review both versions, choose the correct result, test the code, and then complete the merge.

The final Merge Commit has two parents, which preserves the history of both branches.