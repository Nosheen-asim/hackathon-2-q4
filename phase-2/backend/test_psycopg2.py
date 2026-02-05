"""
Test script to verify psycopg2-binary can be imported
"""

try:
    import psycopg2
    print("[SUCCESS] psycopg2-binary imported successfully!")
    print(f"[INFO] psycopg2 version: {psycopg2.__version__}")

    # Test that we can create a connection object (without actually connecting)
    try:
        # This will fail with a connection error, but that's expected
        # The important thing is that importing and basic functionality works
        conn = psycopg2.connect(
            host="dummy",
            database="dummy",
            user="dummy",
            password="dummy"
        )
    except psycopg2.OperationalError:
        # Expected - we don't have a real database to connect to
        print("[INFO] psycopg2 connection functionality available (expected connection error)")
    except Exception as e:
        if "module" in str(e).lower() or "import" in str(e).lower():
            print(f"[ERROR] Issue with psycopg2: {str(e)}")
        else:
            print("[INFO] psycopg2 is working correctly (non-import related error)")

except ImportError as e:
    print(f"[ERROR] Could not import psycopg2-binary: {str(e)}")
except Exception as e:
    print(f"[ERROR] Unexpected error with psycopg2-binary: {str(e)}")