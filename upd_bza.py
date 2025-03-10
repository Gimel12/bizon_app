#!/usr/bin/env python3
import os
import subprocess
import sys

# GitHub repository URL to pull updates from
GITHUB_REPO_URL = "https://github.com/Gimel12/bizon_app.git"
# Default branch to pull from
DEFAULT_BRANCH = "main"

def run_command(cmd, cwd=None):
    """Run a command and return the output and error"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result

def update_app():
    print("\n===== Bizon App Updater =====\n")
    app_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"App directory: {app_dir}")
    
    try:
        # Check if the directory is a git repository
        if not os.path.exists(os.path.join(app_dir, '.git')):
            print("Initializing git repository...")
            run_command(["git", "init"], cwd=app_dir)
            run_command(["git", "remote", "add", "origin", GITHUB_REPO_URL], cwd=app_dir)
            print(f"Added remote origin: {GITHUB_REPO_URL}")
        else:
            # Check current remote URL
            remote_result = run_command(["git", "remote", "-v"], cwd=app_dir)
            current_remote = remote_result.stdout.strip()
            print(f"Current remote: {current_remote}")
            
            # Update remote URL if it's different
            if GITHUB_REPO_URL not in current_remote:
                print(f"Updating remote URL to: {GITHUB_REPO_URL}")
                run_command(["git", "remote", "set-url", "origin", GITHUB_REPO_URL], cwd=app_dir)
        
        # Fetch to get latest branch information
        print("\nFetching latest branch information...")
        fetch_result = run_command(["git", "fetch", "origin"], cwd=app_dir)
        if fetch_result.returncode != 0:
            print(f"Fetch failed: {fetch_result.stderr}")
            return False, fetch_result.stderr
        
        # Get list of remote branches to determine which one to use
        branches_result = run_command(["git", "branch", "-r"], cwd=app_dir)
        remote_branches = branches_result.stdout.strip().split('\n')
        print(f"Available remote branches: {remote_branches}")
        
        # Determine which branch to pull from
        target_branch = DEFAULT_BRANCH
        if f"origin/{DEFAULT_BRANCH}" not in branches_result.stdout:
            if "origin/master" in branches_result.stdout:
                target_branch = "master"
            elif len(remote_branches) > 0:
                # Extract the first branch name without 'origin/' prefix
                first_branch = remote_branches[0].strip()
                if 'origin/' in first_branch:
                    target_branch = first_branch.split('origin/')[1].strip()
        
        print(f"\nPulling from branch: {target_branch}")
        pull_result = run_command(["git", "pull", "origin", target_branch], cwd=app_dir)
        
        if pull_result.returncode == 0:
            print("\n✅ Update successful!")
            print(pull_result.stdout)
            return True, pull_result.stdout
        else:
            print("\n❌ Update failed:")
            print(pull_result.stderr)
            return False, pull_result.stderr
    
    except Exception as e:
        error_msg = f"Error updating app: {str(e)}"
        print(f"\n❌ {error_msg}")
        return False, error_msg


if __name__ == "__main__":
    success, message = update_app()
    print("\n" + "-" * 40)
    print(f"Update {'successful' if success else 'failed'}")
    print("-" * 40 + "\n")
    sys.exit(0 if success else 1)