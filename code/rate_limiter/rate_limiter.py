import time
import threading

class TokenBucketRateLimiter:
    def __init__(self, rate, capacity):
        self.rate = rate                # tokens per second
        self.capacity = capacity        # max tokens in bucket
        self.tokens = capacity
        self.last_check = time.time()
        self.lock = threading.Lock()

    def allow_request(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_check
            added_tokens = elapsed * self.rate
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.last_check = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

# Example usage
if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(rate=2, capacity=5)  # 2 requests per sec

    for i in range(10):
        if limiter.allow_request():
            print(f"✅ Request {i+1} allowed")
        else:
            print(f"❌ Request {i+1} denied - rate limit exceeded")
        time.sleep(0.3)
