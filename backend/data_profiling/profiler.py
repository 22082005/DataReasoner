from .file_profile import get_file_profile
from .data_profile import get_dataset_profile
from .memory_file import get_memory_profile


def profile_dataset(file_path, df):
    """
    Generates a complete dataset profile.
    """

    return {
        "file": get_file_profile(file_path),
        "dataset": get_dataset_profile(df),
        "memory": get_memory_profile(df)
    }