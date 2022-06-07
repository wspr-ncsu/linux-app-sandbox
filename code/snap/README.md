# Snap Data

The initial objective of this project is to pull a list of available applications on the snapcraft store => https://snapcraft.io/store 

SnapDetails.csv content:

Column Name | Description
------------ | -------------
snapName | application name 
snapCategory | application category defined by snapcraft 
snapUrl | application url on snapcraft store 
snapInstallCommand | installation commands recommended by the snapcraft store 

The below steps will provide information on how to refresh the snap file dataset.

### Prerequisites

Python 3.X

### Refreshing Snap Data

After the snap branch is downloaded to your local system the following steps can be followed:

```
cd /local_path/snap
python3 -m venv snap_env
source snap_env/bin/activate
pip install -r requirements.txt
python3 snap.py
```
Refreshing the data can take approximately 7-8 minutes. 

To deactivate the virtual environment:

```
deactivate
```

## Snap Installation Scripts

The module **snap_install.py** will create the initial executable shell scripts and should be executed after the snap dataset is refreshed.

`python3 snap_install.py`

The shell scripts can be found under the **/install_scripts** directory.  

`./install_snap_apps.sh`

Uninstall all applications:

`./uninstall_snap_apps.sh`

## Authors

* **Trevor Dunlap** - *Initial work on pulling snap application data*
