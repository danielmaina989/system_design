# 🔐 Unique ID Generator

This repository demonstrates multiple approaches for generating **unique identifiers** in distributed systems and applications.

## ✅ Implemented Strategies

1. **UUID (Universally Unique Identifier)**
2. **Database Auto-Increment (simulated)**
3. **Range Handler** (partitioned ID space)
4. **UNIX Timestamp + Random**
5. **Snowflake-Inspired Generator**

## 💡 Pros & Cons Overview

| Strategy              | Use Case                                     | Sortable | Globally Unique | Distributed |
|-----------------------|----------------------------------------------|----------|------------------|-------------|
| UUID                  | APIs, tokens, cross-service IDs              | ❌       | ✅               | ✅          |
| Auto-Increment        | Simple apps, relational DBs                  | ✅       | ❌               | ❌          |
| Range Handler         | Multi-node ID space without collisions       | ✅       | ✅               | ✅          |
| Timestamp + Random    | Human-readable or sortable IDs               | ✅       | ✅ (with random) | ✅          |
| Snowflake-like IDs    | Social media, logs, sharded databases        | ✅       | ✅               | ✅          |

## 🧪 Run Examples

```bash
python uuid_gen.py
python db_autoinc_sim.py
python range_handler.py
python unix_time_random.py
python snowflake_sim.py
