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
