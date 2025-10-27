# How to Create a Release

This document explains how to trigger the GitHub Actions workflow to build and release the Coffee Grind Distribution Analyzer application.

## Automatic Release (Recommended)

The workflow automatically triggers when you create and push a version tag:

### Steps:

1. **Make sure all changes are committed and pushed**
   ```bash
   git status
   git push
   ```

2. **Create and push a version tag**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **Wait for the build to complete**
   - Go to the **Actions** tab in your GitHub repository
   - You should see a new workflow run called "Build and Release"
   - Wait for all jobs to complete (usually 5-10 minutes)

4. **Check the release**
   - Go to the **Releases** page
   - You should see a new release with the executables for Windows, macOS, and Linux

## Manual Trigger

You can also manually trigger the workflow without creating a release:

1. Go to the **Actions** tab in your GitHub repository
2. Click on **Build and Release** workflow
3. Click **Run workflow** button
4. Select the branch and click **Run workflow**

Note: This will build the executables but won't create a release (releases are only created for version tags).

## Version Naming Convention

Use semantic versioning for tags:
- `v1.0.0` - Major release
- `v1.1.0` - Minor release with new features
- `v1.0.1` - Patch release with bug fixes

## Troubleshooting

If the workflow fails:
1. Check the workflow logs in the Actions tab
2. Common issues:
   - Python syntax errors in app.py
   - Missing dependencies in requirements.txt
   - YAML syntax errors in the workflow file

## Testing Before Release

Before creating a version tag, you can:
1. Use the manual trigger to test the build
2. Run the test suite locally: `python3 test_app.py`
3. Verify the application works: `python3 app.py` (requires tkinter)
