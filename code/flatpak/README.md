# Flatpak Manifest Files

The objective of this project is to pull the manifest files for all of the flatpak applications on flathub.org. The manifest file will provide valuable insight into the sandbox permission configurations for flatpak applications. 

### Prerequisites

Python 3.X

### Refreshing Manifest Data

he following steps can be followed to refresh data:

```
cd /local_path/flatpak
python3 -m venv flatpaks_env
source flatpaks_env/bin/activate
pip install -r requirements.txt
python3 flatpak_manifest.py
```
To deactivate the virtual environment:
```
deactivate
```

## Authors

* **Trevor Dunlap** - *Initial work on pulling flatpak manifest files*


