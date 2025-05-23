# 🗂️ Blob Store (Binary Large Object Storage)

A simple and efficient Python implementation of a blob store for managing large binary files such as images, backups, and videos.

## 📦 Features

- **Content-addressable storage:** Uses SHA256 hash as a unique Blob ID for deduplication and integrity.
- **Local storage backend:** Stores blobs in a configurable directory structure.
- **Upload and download API:** Simple interface for adding and retrieving blobs.
- **Efficient handling:** Designed for large files, supports streaming to minimize memory usage.
- **Metadata support:** Optionally stores metadata alongside blobs.
- **Easy integration:** Minimal dependencies, suitable for embedding in other Python projects.

## 🧪 Usage

### Initialize the Blob Store

```python
from blob_store import BlobStore

store = BlobStore("/path/to/blob_storage")
```

### Upload a File

```python
blob_id = store.upload("example.png")
print(f"Uploaded blob with ID: {blob_id}")
```

### Download a File

```python
store.download(blob_id, "restored_example.png")
print("File downloaded successfully.")
```

### Check if a Blob Exists

```python
exists = store.exists(blob_id)
print(f"Blob exists: {exists}")
```

### Delete a Blob

```python
store.delete(blob_id)
print("Blob deleted.")
```

## 🗃️ Storage Structure

Blobs are stored in subdirectories based on the prefix of their SHA256 hash to avoid filesystem limits.

Example:
```
/blob_storage/ab/cd/abcdef1234567890...
```

## 🚀 Example Use Cases

- Backup and restore systems
- Media storage for web applications
- Caching large files by content hash
- Deduplicating binary data

## 📄 License

MIT License. See [LICENSE](./LICENSE) for details.
