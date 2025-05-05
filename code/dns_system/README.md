# DNS System Simulation

This is a simplified Python simulation of the Domain Name System (DNS) resolution process.

## 💡 What It Simulates

- Local DNS cache
- Root DNS server
- Top-Level Domain (TLD) server
- Authoritative server

## 📄 How It Works

1. Tries to resolve from local cache
2. Queries root server to find the TLD server
3. Queries TLD server to find the authoritative server
4. Queries authoritative server for the final IP
5. Caches the result in local cache

## ▶️ Run the Simulation

```bash
cd code/dns_system
python main.py
