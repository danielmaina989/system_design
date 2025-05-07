"""
Compare relational (table-like) and non-relational (document-like) databases using simple examples.
"""

# Relational (like SQL)
relational_db = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
}

# Non-Relational (like MongoDB)
nosql_db = {
    "users": {
        "user1": {"name": "Alice", "likes": ["cats", "books"]},
        "user2": {"name": "Bob", "age": 30},
    }
}

def show_relational():
    print("\n🧱 Relational DB (Table Style):")
    for row in relational_db["users"]:
        print(row)

def show_nosql():
    print("\n📦 NoSQL DB (Document Style):")
    for doc_id, content in nosql_db["users"].items():
        print(f"{doc_id}: {content}")

if __name__ == "__main__":
    show_relational()
    show_nosql()
