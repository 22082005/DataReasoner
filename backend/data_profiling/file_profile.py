from pathlib import Path


def get_file_profile(file_path):
    """
    Returns metadata about the uploaded file.
    """

    file_path = Path(file_path)

    size_bytes = file_path.stat().st_size

    return {
        "file_name": file_path.name,
        "extension": file_path.suffix.lower(),
        "size_bytes": size_bytes,
        "size_kb": round(size_bytes / 1024, 2),
        "size_mb": round(size_bytes / (1024 * 1024), 2)
    }