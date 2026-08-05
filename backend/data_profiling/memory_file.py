def get_memory_profile(df):
    """
    Returns DataFrame memory usage.
    """

    memory_bytes = df.memory_usage(deep=True).sum()

    return {
        "memory_bytes": int(memory_bytes),
        "memory_kb": round(memory_bytes / 1024, 2),
        "memory_mb": round(memory_bytes / (1024 * 1024), 4)
    }