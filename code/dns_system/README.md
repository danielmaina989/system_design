# 🧠 DNS System Simulation

This is a simplified Python simulation of the Domain Name System (DNS) resolution process.

## 💡 What It Simulates

- Local DNS cache
- Root DNS server
- Top-Level Domain (TLD) server
- Authoritative DNS server
- Recursive and Iterative resolution modes

## 📁 Project Structure


## 📄 How It Works

### `main.py` – Basic DNS Lookup Flow:
1. Tries to resolve from local cache
2. Queries root server to find the TLD server
3. Queries TLD server to find the authoritative server
4. Queries authoritative server for the final IP
5. Caches the result in local cache

### `dns_query_types.py` – Recursive vs Iterative:
- **Recursive Query**: Local resolver does all the work and returns the final IP.
- **Iterative Query**: Resolver queries each layer step-by-step, guided by each server.

## 🖼️ Visual Diagram

See `diagrams/dns_lookup_process.png` for a clear breakdown of the DNS query flow:

![DNS Lookup Process](diagrams/dns_lookup_process.png)

## ▶️ Run the Simulation

```bash
cd code/dns_system

# Run simple DNS resolution
python main.py

# Run recursive vs iterative resolution
python dns_query_types.py
