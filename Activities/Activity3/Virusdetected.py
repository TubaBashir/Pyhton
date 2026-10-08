import hashlib
import os

# 1. Database of known malicious SHA-256 file hashes (Example sample hashes)
KNOWN_MALICIOUS_HASHES = {
    # Replace with real SHA-256 hashes you want to flag
    "44d88612fea8a8f36de82e1278abb02f": "EICAR-Test-File",
    "d41d8cd98f00b204e9800998ecf8427e": "Empty-File-Signature",
}

# 2. Heuristic keyword / string patterns common in malicious scripts
SUSPICIOUS_STRINGS = [
    b"rd /s /q c:\\",
    b"rm -rf /",
    b"Invoke-WebRequest",
    b"WScript.Shell",
]


def calculate_sha256(file_path):
    """Calculates the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[-] Error reading {file_path}: {e}")
        return None


def scan_file(file_path):
    """Scans a single file using hash matching and heuristic string inspection."""
    file_hash = calculate_sha256(file_path)
    if not file_hash:
        return

    # Check against known malicious hashes
    if file_hash in KNOWN_MALICIOUS_HASHES:
        threat_name = KNOWN_MALICIOUS_HASHES[file_hash]
        print(f"[!] ALERT: Known virus detected ({threat_name}) in: {file_path}")
        return True

    # Check file contents for suspicious heuristics
    try:
        with open(file_path, "rb") as f:
            content = f.read()
            for pattern in SUSPICIOUS_STRINGS:
                if pattern in content:
                    print(
                        f"[!] ALERT: Suspicious pattern {pattern.decode('utf-8', errors='ignore')} found in: {file_path}"
                    )
                    return True
    except Exception:
        pass

    print(f"[+] Clean: {file_path}")
    return False


def scan_directory(directory_path):
    """Recursively scans all files in a given directory."""
    print(f"[*] Starting scan on directory: {directory_path}\n")
    infected_count = 0
    total_files = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            total_files += 1
            if scan_file(full_path):
                infected_count += 1

    print(
        f"\n[*] Scan complete. Scanned {total_files} files. Threats found: {infected_count}"
    )


if __name__ == "__main__":
    # Example target directory to scan (change to your test folder)
    target_dir = "./test_files"
    if os.path.exists(target_dir):
        scan_directory(target_dir)
    else:
        print(f"Directory '{target_dir}' does not exist. Create it and add files to test.")
