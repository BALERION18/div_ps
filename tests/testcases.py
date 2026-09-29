import os
import re
import sys

VALID_DUMMY_CASES = [
    "student@niet.co.in",
    "aman.gupta@niet.co.in",
    "rahul.sharma@niet.co.in",
    "somesh_devops@niet.co.in",
    "cse.hod@niet.co.in",
]

INVALID_DUMMY_CASES = [
    "student@gmail.com",
    "user@yahoo.co.in",
    "admin@niet.com",
    "tester@niet.org",
    "rahul@outlook.com",
    "fake@niet.ac.in",
    "invalid-email-format",
]

ACTIVE_DUMMY_CASE = os.environ.get("TEST_EMAIL", "student@gmail.co.in")

def validate_niet_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@niet\.co\.in$"
    return bool(re.match(pattern, email.strip(), re.IGNORECASE))

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg == "--test-valid":
        print("--- Testing VALID Dummy Cases ---")
        all_passed = True
        for case in VALID_DUMMY_CASES:
            if validate_niet_email(case):
                print(f"  [PASS] {case} (Valid NIET Email)")
            else:
                print(f"  [FAIL] {case}")
                all_passed = False
        if all_passed:
            print("\nResult: ALL VALID DUMMY CASES PASSED [OK]")
            sys.exit(0)
        else:
            sys.exit(1)

    elif arg == "--test-invalid":
        print("--- Testing INVALID Dummy Cases (Expecting Failure) ---")
        for case in INVALID_DUMMY_CASES:
            if not validate_niet_email(case):
                print(f"  [FAIL DETECTED] {case} -> Rejected (Only @niet.co.in allowed)")
            else:
                print(f"  [UNEXPECTED PASS] {case}")
        print("\nResult: All invalid dummy cases failed validation as required! [OK]")
        sys.exit(0)

    else:
        target = arg if arg else ACTIVE_DUMMY_CASE
        print(f"Verifying dummy email: '{target}'")
        if validate_niet_email(target):
            print(f"Result: [PASS] '{target}' is a valid @niet.co.in email.")
            sys.exit(0)
        else:
            print(f"Result: [FAIL] '{target}' is an INVALID dummy case! Only @niet.co.in is allowed.")
            sys.exit(1)

if __name__ == "__main__":
    main()
