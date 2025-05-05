# main.py

"""
A basic simulation of the Domain Name System (DNS) resolution process.
We simulate a local DNS cache, root server, TLD server, and authoritative server.
"""

# Simulated DNS hierarchy

# Local DNS cache (fastest lookup)
local_cache = {
    "example.com": "93.184.216.34"
}

# Root DNS server (delegates to TLD)
root_server = {
    "com": "tld_com_server"
}

# TLD DNS server (delegates to authoritative)
tld_servers = {
    "tld_com_server": {
        "example.com": "auth_example_server"
    }
}

# Authoritative DNS server (final IP address)
auth_servers = {
    "auth_example_server": {
        "example.com": "93.184.216.34"
    }
}


def resolve(domain):
    print(f"Resolving domain: {domain}")

    # Step 1: Check local cache
    if domain in local_cache:
        print("✔️ Found in local cache.")
        return local_cache[domain]

    print("🔍 Not in local cache. Querying root DNS server...")

    # Step 2: Query root server
    tld = domain.split(".")[-1]
    tld_server_name = root_server.get(tld)
    if not tld_server_name:
        print("❌ TLD not found in root server.")
        return None

    print(f"📡 Root server points to TLD server: {tld_server_name}")

    # Step 3: Query TLD server
    tld_server = tld_servers.get(tld_server_name)
    if not tld_server or domain not in tld_server:
        print("❌ Domain not found in TLD server.")
        return None

    auth_server_name = tld_server[domain]
    print(f"📡 TLD server points to authoritative server: {auth_server_name}")

    # Step 4: Query authoritative server
    ip_address = auth_servers.get(auth_server_name, {}).get(domain)
    if not ip_address:
        print("❌ Domain not found in authoritative server.")
        return None

    print(f"✔️ Found in authoritative server. IP: {ip_address}")
    print("💾 Caching in local DNS...")
    local_cache[domain] = ip_address  # Cache the result

    return ip_address


# Example usage
if __name__ == "__main__":
    domain_to_resolve = "example.com"
    ip = resolve(domain_to_resolve)
    print(f"\n🔗 Final IP address for {domain_to_resolve}: {ip}")


# dns_query_types.py

"""
Simulate the difference between recursive and iterative DNS query resolution.
"""

# Simulated DNS data
root_server = {
    "com": "tld_com_server"
}

tld_servers = {
    "tld_com_server": {
        "example.com": "auth_example_server"
    }
}

auth_servers = {
    "auth_example_server": {
        "example.com": "93.184.216.34"
    }
}

# ------------------------------
# RECURSIVE DNS RESOLUTION
# ------------------------------
def recursive_resolve(domain):
    print("\n🔁 Recursive DNS Resolution")
    return recursive_helper(domain)


def recursive_helper(domain):
    print("Local DNS resolver starts recursion...")
    tld = domain.split(".")[-1]

    # Ask root server
    tld_server = root_server.get(tld)
    if not tld_server:
        print("❌ TLD not found at root level")
        return None

    # Ask TLD server
    auth_server = tld_servers.get(tld_server, {}).get(domain)
    if not auth_server:
        print("❌ Domain not found at TLD level")
        return None

    # Ask Authoritative server
    ip = auth_servers.get(auth_server, {}).get(domain)
    if not ip:
        print("❌ IP not found at authoritative level")
        return None

    print(f"✅ Final IP from authoritative server: {ip}")
    return ip


# ------------------------------
# ITERATIVE DNS RESOLUTION
# ------------------------------
def iterative_resolve(domain):
    print("\n🔄 Iterative DNS Resolution")
    print("User queries local resolver...")

    # Local resolver queries root
    print("Local resolver asks Root server...")
    tld = domain.split(".")[-1]
    tld_server = root_server.get(tld)
    if not tld_server:
        print("❌ TLD not found")
        return None

    print(f"Root server returns TLD server: {tld_server}")

    # Local resolver queries TLD
    print("Local resolver asks TLD server...")
    auth_server = tld_servers.get(tld_server, {}).get(domain)
    if not auth_server:
        print("❌ Domain not found at TLD server")
        return None

    print(f"TLD server returns authoritative server: {auth_server}")

    # Local resolver queries authoritative
    print("Local resolver asks Authoritative server...")
    ip = auth_servers.get(auth_server, {}).get(domain)
    if not ip:
        print("❌ IP not found at authoritative server")
        return None

    print(f"✅ Final IP from authoritative server: {ip}")
    return ip


# ------------------------------
# Run examples
# ------------------------------
if __name__ == "__main__":
    domain = "example.com"
    ip1 = recursive_resolve(domain)
    print(f"\n🔗 Recursive: IP address of {domain} is {ip1}")

    ip2 = iterative_resolve(domain)
    print(f"\n🔗 Iterative: IP address of {domain} is {ip2}")
