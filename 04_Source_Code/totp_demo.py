"""Optional TOTP feasibility demonstration.

Requires the third-party PyOTP package listed in requirements.txt.
No secret is stored in the repository; a temporary demo secret is generated at runtime.
This file is not a production authenticator implementation.
"""
try:
    import pyotp
except ImportError as exc:
    raise SystemExit("PyOTP is not installed. Run: python -m pip install -r 04_Source_Code/requirements.txt") from exc


def main() -> None:
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    print("Temporary demo secret (do not use in production):", secret)
    print("Current demo TOTP:", totp.now())
    print("Verification check:", totp.verify(totp.now()))


if __name__ == "__main__":
    main()
