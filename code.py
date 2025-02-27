import hashlib

def weak_hash_test(data):

    sha1_result = hashlib.sha1(data.encode()).hexdigest()
    md5_result = hashlib.md5(data.encode()).hexdigest()

    print(f"[!] SHA-1 hash key: {sha1_result}")
    print(f"[-] MD5 hash key: {md5_result}")
    print("This algorithm is no longer recommended")


weak_hash_test("test_password")
