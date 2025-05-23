# 🚦 Rate Limiter — Token Bucket Algorithm

A simple Python implementation of a rate limiter using the Token Bucket algorithm.

## 📖 Overview

The Token Bucket algorithm controls the rate at which actions are performed. It is commonly used to limit requests to APIs or other resources.

## 🔧 How It Works

- Each incoming request consumes one token from the bucket.
- Tokens are added to the bucket at a fixed rate (`rate` tokens per second).
- The bucket has a maximum capacity (`capacity`). Extra tokens are discarded if the bucket is full.
- If a request arrives when no tokens are available, it is denied or delayed.

## ⚙️ Configuration

- **`rate`**: Number of tokens added to the bucket per second.
- **`capacity`**: Maximum number of tokens the bucket can hold.

## 🚀 Usage

1. Clone the repository and navigate to the project directory.
2. Run the rate limiter script:

    ```bash
    python rate_limiter.py
    ```

3. Adjust `rate` and `capacity` in the script as needed for your use case.

## 📝 Example

```python
from rate_limiter import RateLimiter

limiter = RateLimiter(rate=5, capacity=10)

if limiter.allow_request():
     print("Request allowed")
else:
     print("Rate limit exceeded")
```

## 📂 Files

- `rate_limiter.py` — Implementation of the Token Bucket rate limiter.
- `README.md` — Project documentation.

## 📄 License

This project is licensed under the MIT License.
