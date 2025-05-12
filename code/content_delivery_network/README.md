# 🌐 CDN Simulation in Python

This project simulates a simplified **Content Delivery Network (CDN)** in Python to demonstrate how edge caching works.

🧩 Explanation
Push CDN: Content is manually uploaded to edge servers in advance. Good for static, infrequently updated content.

Pull CDN: Edge servers fetch content on-demand from the origin server when a request is made. Most modern CDNs use this model.



## 📌 What’s Covered

- Origin server
- Edge servers across different regions
- Cache TTL (Time To Live)
- Cache expiration and refresh from origin

## 🚀 How It Works

1. When a file is requested:
   - It first checks the corresponding **regional edge server**.
   - If cached and not expired → serves from the edge.
   - If expired or not present → fetches from origin and caches it.
2. Each region has its **own cache** and **TTL tracker**.

## ▶️ Run the Simulation

```bash
python main.py

# 📦 CDN Models: Push vs Pull

This example demonstrates the difference between **Push** and **Pull** models used in Content Delivery Networks (CDNs).

---

## 🔁 Models Explained

- **Push CDN**
  - You upload (push) content to the edge manually.
  - Requires you to manage cache and updates.
  - Ideal for static content like images, scripts.

- **Pull CDN**
  - Content is fetched on request from origin if not already cached.
  - Most widely used.
  - Requires cache invalidation strategy.

---

## 🚀 How to Run

```bash
python main.py

