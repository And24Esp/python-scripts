import os
import ctypes
from collections import Counter
from ctypes import wintypes

def get_dirlist(path):
    """Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names."""
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

class CloudFilesPlaceholderInfo(ctypes.Structure):
    """Subset of CF_PLACEHOLDER_STANDARD_INFO needed for sync status."""
    _fields_ = [
        ("on_disk_data_size", ctypes.c_longlong),
        ("validated_data_size", ctypes.c_longlong),
        ("modified_data_size", ctypes.c_longlong),
        ("properties_size", ctypes.c_longlong),
        ("pin_state", wintypes.DWORD),
        ("in_sync_state", wintypes.DWORD),
        ("file_id", ctypes.c_longlong),
        ("sync_root_file_id", ctypes.c_longlong),
        ("file_identity_length", wintypes.DWORD),
        ("file_identity", ctypes.c_ubyte * 4096),
    ]


def get_onedrive_sync_status(path):
    """Return the Cloud Files synchronization status for path."""
    if os.name != "nt":
        return "Unavailable (Windows only)"

    create_file = ctypes.windll.kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
        wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE

    close_handle = ctypes.windll.kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL

    handle = create_file(
        str(path),
        0x0080,  # FILE_READ_ATTRIBUTES
        0x00000007,  # FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE
        None,
        3,  # OPEN_EXISTING
        0x02000000 if os.path.isdir(path) else 0,  # FILE_FLAG_BACKUP_SEMANTICS
        None,
    )
    if handle == wintypes.HANDLE(-1).value:
        return "Unavailable" # "Unavailable": The script could not inspect the item at all, usually because Windows could not open it or the script is running on a non-Windows system.

    try:
        placeholder_info = CloudFilesPlaceholderInfo()
        returned_length = wintypes.DWORD()
        get_placeholder_info = ctypes.windll.CldApi.CfGetPlaceholderInfo
        get_placeholder_info.argtypes = [
            wintypes.HANDLE, wintypes.DWORD, wintypes.LPVOID,
            wintypes.DWORD, ctypes.POINTER(wintypes.DWORD),
        ]
        get_placeholder_info.restype = ctypes.c_long
        result = get_placeholder_info(
            handle,
            1,  # CF_PLACEHOLDER_INFO_STANDARD
            ctypes.byref(placeholder_info),
            ctypes.sizeof(placeholder_info),
            ctypes.byref(returned_length),
        )
        if result != 0:
            return "Not a cloud placeholder" # "Not a cloud placeholder": Windows opened the file successfully, but OneDrive’s Cloud Files API says the file is not managed as a cloud placeholder. It may be a regular local file or folder.
        if placeholder_info.in_sync_state == 1:
            return "In sync"
        return "Sync pending"
    finally:
        close_handle(handle)

def get_file_status_counts(path):
    """Return the number of files in each OneDrive synchronization state."""
    status_counts = Counter({
        "In sync": 0,
        "Sync pending": 0,
        "Not a cloud placeholder": 0,
        "Unavailable": 0,
    })

    for entry in get_dirlist(path):
        fullname = os.path.join(path, entry)
        if os.path.isdir(fullname):
            status_counts.update(get_file_status_counts(fullname))
        else:
            status_counts[get_onedrive_sync_status(fullname)] += 1

    return status_counts

def print_summary(path):
    """Print an executive summary of file counts by synchronization state."""
    status_counts = get_file_status_counts(path)
    print("Executive summary")
    for status, count in status_counts.items():
        print(f"{status}: {count} file(s)")
    print()

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)   # Turn name into full pathname
        status = get_onedrive_sync_status(fullname)
        print(f"{prefix}{f} | ODS {status}") #ODS=One Drive Status
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")

root_path = 'C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\02 Computer Science'
print_files(root_path)
print_summary(root_path)