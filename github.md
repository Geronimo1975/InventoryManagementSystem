1. Install Git
First, ensure Git is installed:

bash
Copy code
sudo apt update
sudo apt install git
git --version
2. Configure Git
Set your global username and email (used for commits):

bash
Copy code
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
3. Clone the Repository
If the repository is already created on GitHub:

bash
Copy code
git clone https://github.com/username/repository.git
cd repository
If you need to create a new repository:

bash
Copy code
mkdir project-name
cd project-name
git init
Then create a repository on GitHub and link it:

bash
Copy code
git remote add origin https://github.com/username/repository.git
git branch -M main
git push -u origin main
4. Branch Management
To create and switch to a new feature branch:

bash
Copy code
git checkout -b feature-branch-name
Push the new branch to GitHub:

bash
Copy code
git push -u origin feature-branch-name
5. Sync Changes
Pull the latest changes from the main branch:

bash
Copy code
git checkout main
git pull origin main
Merge changes into your branch:

bash
Copy code
git checkout feature-branch-name
git merge main
6. Add, Commit, and Push Changes
Stage changes:

bash
Copy code
git add .
Commit changes with a message:

bash
Copy code
git commit -m "Describe your changes"
Push to your branch:

bash
Copy code
git push
7. Submit Pull Requests
After pushing your branch to GitHub:

Visit the repository on GitHub.
Click Compare & Pull Request.
Add a description and submit the pull request for review.
8. Resolve Merge Conflicts
If there are conflicts:

Git will notify you after pulling or merging.
Open conflicting files, resolve the conflicts manually, and stage them:
bash
Copy code
git add conflict-file-name
Commit the resolved changes:
bash
Copy code
git commit
9. Setup .gitignore
Create a .gitignore file to exclude unnecessary files:

bash
Copy code
nano .gitignore
Add common patterns (e.g., for Python, Node.js):

bash
Copy code
# Example for Python
*.pyc
__pycache__/

# Example for Node.js
node_modules/
Save and exit, then commit the file:

bash
Copy code
git add .gitignore
git commit -m "Add .gitignore file"
10. Install Dependencies (Optional)
For consistent environments, use requirements.txt (Python) or package.json (Node.js).

Python:

bash
Copy code
pip install -r requirements.txt
Node.js:

bash
Copy code
npm install
11. Collaborative Tools
Set Up Pre-Commit Hooks
Install pre-commit:

bash
Copy code
pip install pre-commit
pre-commit install
Add a .pre-commit-config.yaml:

bash
Copy code
nano .pre-commit-config.yaml
Example for Python:

yaml
Copy code
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
Commit the configuration:

bash
Copy code
git add .pre-commit-config.yaml
git commit -m "Add pre-commit hooks"
12. Automate with GitHub Actions
Create a workflow file:

bash
Copy code
mkdir -p .github/workflows
nano .github/workflows/ci.yml
Example for a Python project:

yaml
Copy code
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
Push it to the repository:

bash
Copy code
git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions workflow"
git push
