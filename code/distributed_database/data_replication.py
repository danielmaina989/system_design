"""
Simulate data replication: Primary writes data, secondaries receive the update.
"""

primary_db = []
replica_dbs = {
    "replica_1": [],
    "replica_2": [],
}

def write_to_primary(data):
    print(f"\n📝 Writing to Primary DB: {data}")
    primary_db.append(data)
    replicate(data)

def replicate(data):
    print("🔄 Replicating to replicas...")
    for name in replica_dbs:
        replica_dbs[name].append(data)
        print(f"✅ {name} updated")

if __name__ == "__main__":
    write_to_primary({"id": 1, "name": "Alice"})
    write_to_primary({"id": 2, "name": "Bob"})

    print("\n📌 Final DB States:")
    print(f"Primary: {primary_db}")
    for name, db in replica_dbs.items():
        print(f"{name}: {db}")
