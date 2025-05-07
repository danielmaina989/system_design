"""
Simulate a distributed file storage system where files are stored across nodes.
"""

file_storage = {
    "node_1": [],
    "node_2": [],
    "node_3": [],
}

def store_file(filename):
    # Round-robin storage simulation
    node = min(file_storage, key=lambda k: len(file_storage[k]))
    file_storage[node].append(filename)
    print(f"📦 Stored '{filename}' in {node}")

if __name__ == "__main__":
    files = ["photo1.jpg", "video.mp4", "doc.pdf", "slide.pptx", "notes.txt"]
    for f in files:
        store_file(f)

    print("\n🗂️ File Distribution:")
    for node, files in file_storage.items():
        print(f"{node}: {files}")
