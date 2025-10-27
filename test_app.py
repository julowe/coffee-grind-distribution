#!/usr/bin/env python3
"""
Simple test to verify the Coffee Grind Distribution Analyzer application structure
"""

import sys
import os

def test_app_imports():
    """Test that the app can be imported without GUI dependencies"""
    # Add current directory to path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Try to parse the app file for syntax errors
    with open('app.py', 'r') as f:
        code = f.read()
        try:
            compile(code, 'app.py', 'exec')
            print("✓ app.py syntax is valid")
            return True
        except SyntaxError as e:
            print(f"✗ Syntax error in app.py: {e}")
            return False

def test_required_files():
    """Test that all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        '.github/workflows/build-release.yml',
        'README.md',
        '.gitignore'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_readme_content():
    """Test that README has been updated with download instructions"""
    with open('README.md', 'r') as f:
        content = f.read()
        
    checks = [
        ('Download the Application', 'Download section'),
        ('Releases page', 'Releases link'),
        ('CoffeeGrindAnalyzer', 'Application name'),
        ('Windows', 'Windows instructions'),
        ('macOS', 'macOS instructions'),
        ('Linux', 'Linux instructions'),
    ]
    
    all_present = True
    for search_term, description in checks:
        if search_term in content:
            print(f"✓ README contains {description}")
        else:
            print(f"✗ README missing {description}")
            all_present = False
    
    return all_present

if __name__ == "__main__":
    print("Running tests...\n")
    
    results = []
    
    print("Test 1: Application Imports")
    results.append(test_app_imports())
    
    print("\nTest 2: Required Files")
    results.append(test_required_files())
    
    print("\nTest 3: README Content")
    results.append(test_readme_content())
    
    print("\n" + "="*50)
    if all(results):
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)
