#!/usr/bin/env python3
"""
Simple test script for card_generator.py
"""

import os
import sys
import subprocess


def run_test(test_name, command, expected_file):
    """Run a test and verify the output"""
    print(f"\n{'='*60}")
    print(f"Test: {test_name}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    # Remove old file if exists
    if os.path.exists(expected_file):
        os.remove(expected_file)
    
    # Run command
    result = subprocess.run(command.split(), capture_output=True, text=True)
    
    # Check if successful
    if result.returncode != 0:
        print(f"❌ FAILED: Command returned error code {result.returncode}")
        print(f"Error: {result.stderr}")
        return False
    
    # Check if file was created
    if not os.path.exists(expected_file):
        print(f"❌ FAILED: Expected file '{expected_file}' was not created")
        return False
    
    # Check file size
    file_size = os.path.getsize(expected_file)
    if file_size == 0:
        print(f"❌ FAILED: Generated file is empty")
        return False
    
    print(f"✅ PASSED: Generated {expected_file} ({file_size} bytes)")
    print(f"Output: {result.stdout}")
    
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("Card Generator Test Suite")
    print("=" * 60)
    
    tests = [
        ("Default usage (1-99)", f"{sys.executable} card_generator.py -o test_default.pdf", "test_default.pdf"),
        ("Small range (1-5)", f"{sys.executable} card_generator.py -n 1-5 -o test_small.pdf", "test_small.pdf"),
        ("Specific numbers", f"{sys.executable} card_generator.py -n 10,20,30 -o test_specific.pdf", "test_specific.pdf"),
        ("Complex range", f"{sys.executable} card_generator.py -n 1-10,15,20-25 -o test_complex.pdf", "test_complex.pdf"),
        ("Custom dimensions", f"{sys.executable} card_generator.py -w 70 --height 100 -n 1-5 -o test_custom.pdf", "test_custom.pdf"),
    ]
    
    passed = 0
    failed_count = 0
    
    for test_name, command, expected_file in tests:
        if run_test(test_name, command, expected_file):
            passed += 1
        else:
            failed_count += 1
    
    # Clean up test files
    print(f"\n{'='*60}")
    print("Cleaning up test files...")
    for _, _, expected_file in tests:
        if os.path.exists(expected_file):
            os.remove(expected_file)
            print(f"Removed {expected_file}")
    
    # Summary
    print(f"\n{'='*60}")
    print("Test Summary")
    print(f"{'='*60}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed_count}")
    print(f"Total: {passed + failed_count}")
    print(f"{'='*60}")
    
    return 0 if failed_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
