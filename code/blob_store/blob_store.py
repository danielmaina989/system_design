import os
import hashlib
from datetime import datetime

class BlobStore:
    def __init__(self, storage_dir='blob_storage'):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _generate_blob_id(self, content):
        # Use SHA256 hash to generate unique blob ID
        return hashlib.sha256(content).hexdigest()

    def upload(self, file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
            blob_id = self._generate_blob_id(content)
            blob_path = os.path.join(self.storage_dir, blob_id)
            with open(blob_path, 'wb') as blob_file:
                blob_file.write(content)
            return blob_id

    def download(self, blob_id, destination_path):
        blob_path = os.path.join(self.storage_dir, blob_id)
        if os.path.exists(blob_path):
            with open(blob_path, 'rb') as blob_file:
                with open(destination_path, 'wb') as dest_file:
                    dest_file.write(blob_file.read())
            return True
        return False

# Example usage
if __name__ == "__main__":
    store = BlobStore()

    blob_id = store.upload("example.png")
    print(f"✅ Uploaded blob ID: {blob_id}")

    success = store.download(blob_id, "downloaded_example.png")
    print("✅ Download successful" if success else "❌ Blob not found")
