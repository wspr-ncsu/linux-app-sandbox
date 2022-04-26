## Device Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
| Flatpak | coarse-grained | --device=all |
| Flatpak | fine-grained | --system-talk-name=org.bluez |
| Flatpak | fine-grained | --socket=cups |
| Flatpak | fine-grained | --socket=pcsc |
| Flatpak | fine-grained | --socket=pulseaudio |
| Flatpak | fine-grained | --device=shm |
| Snap | fine-grained | alsa |
| Snap | fine-grained | audio-playback |
| Snap | fine-grained | audio-record |
| Snap | fine-grained | block-devices |
| Snap | fine-grained | bluetooth-control |
| Snap | fine-grained | bluez |
| Snap | fine-grained | camera |
| Snap | fine-grained | cups-control |
| Snap | fine-grained | dvb |
| Snap | fine-grained | hardware-observe |
| Snap | fine-grained | jack1 |
| Snap | fine-grained | joystick |
| Snap | fine-grained | optical-drive |
| Snap | fine-grained | optical-write |
| Snap | fine-grained | physical-memory-observe |
| Snap | fine-grained | pulseaudio |
| Snap | fine-grained | raw-usb |
| Snap | fine-grained | removable-media |
| Snap | fine-grained | serial-port |
| Snap | fine-grained | u2f-devices |


## Filesystem Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
|Flatpak | coarse-grained | --filesystem=home |
|Flatpak | coarse-grained | --filesystem=host |
|Flatpak | fine-grained | --filesystem=xdg |
|Flatpak | fine-grained | --filesystem=/some/path |
|Flatpak | fine-grained | --filesystem=~/some/path |
| Snap | coarse-grained | home |
| Snap | coarse-grained | classic |
| Snap | fine-grained | personal-files |


## Graphics Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
| Flatpak | fine-grained | --device=dri |
| Flatpak | fine-grained | --share=ipc |
| Flatpak | fine-grained | --socket=fallback-x11 |
| Flatpak | fine-grained | --socket=wayland |
| Flatpak | fine-grained | --socket=x11 |
| Flatpak | fine-grained | --talk-name=org.gnome.Mutter.IdleMonitor |
| Snap | fine-grained | desktop |
| Snap | fine-grained | desktop-legacy |
| Snap | fine-grained | mir |
| Snap | fine-grained | opengl |
| Snap | fine-grained | unity7 |
| Snap | fine-grained | wayland |
| Snap | fine-grained | x11 |


## Network Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
| Flatpak | coarse-grained | --share=network |
| Snap | coarse-grained | network |
| Snap | coarse-grained | network-bind |


## Session IPC Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
| Flatpak | coarse-grained | --socket=session-bus |
| Flatpak | fine-grained | --socket=ssh-auth |
| Flatpak | fine-grained | --talk-name=ca.desrt.dconf |
| Flatpak | fine-grained | --talk-name=com.canonical.AppMenu.Registrar |
| Flatpak | fine-grained | --talk-name=com.canonical.AppMenu.Registrar.* |
| Flatpak | fine-grained | --talk-name=com.canonical.indicator.application |
| Flatpak | fine-grained | --talk-name=com.canonical.Unity |
| Flatpak | fine-grained | --talk-name=com.canonical.Unity.LauncherEntry |
| Flatpak | fine-grained | --talk-name=com.canonical.Unity.Session |
| Flatpak | fine-grained | --talk-name=net.launchpad.DockManager |
| Flatpak | fine-grained | --talk-name=org.a11y.* |
| Flatpak | fine-grained | --talk-name=org.a11y.Bus |
| Flatpak | fine-grained | --talk-name=org.ayatana.indicator.application |
| Flatpak | fine-grained | --talk-name=org.freedesktop.DockManager |
| Flatpak | fine-grained | --talk-name=org.freedesktop.FileManager |
| Flatpak | fine-grained | --talk-name=org.freedesktop.FileManager1 |
| Flatpak | fine-grained | --talk-name=org.freedesktop.Flatpak |
| Flatpak | fine-grained | --talk-name=org.freedesktop.login1.Manager |
| Flatpak | fine-grained | --talk-name=org.freedesktop.login1.Session |
| Flatpak | fine-grained | --talk-name=org.freedesktop.Notifications |
| Flatpak | fine-grained | --talk-name=org.freedesktop.portal.Fcitx |
| Flatpak | fine-grained | --talk-name=org.freedesktop.portal.Screenshot |
| Flatpak | fine-grained | --talk-name=org.freedesktop.PowerManagement |
| Flatpak | fine-grained | --talk-name=org.freedesktop.PowerManagement.Inhibit |
| Flatpak | fine-grained | --talk-name=org.freedesktop.ScreenSaver |
| Flatpak | fine-grained | --talk-name=org.freedesktop.secrets |
| Flatpak | fine-grained | --talk-name=org.gnome.ControlCenter |
| Flatpak | fine-grained | --talk-name=org.gnome.evolution.dataserver.AddressBook10 |
| Flatpak | fine-grained | --talk-name=org.gnome.evolution.dataserver.AddressBook9 |
| Flatpak | fine-grained | --talk-name=org.gnome.evolution.dataserver.Calendar8 |
| Flatpak | fine-grained | --talk-name=org.gnome.evolution.dataserver.Sources5 |
| Flatpak | fine-grained | --talk-name=org.gnome.evolution.dataserver.Subprocess.Backend.* |
| Flatpak | fine-grained | --talk-name=org.gnome.GConf |
| Flatpak | fine-grained | --talk-name=org.gnome.OnlineAccounts |
| Flatpak | fine-grained | --talk-name=org.gnome.ScreenSaver |
| Flatpak | fine-grained | --talk-name=org.gnome.SessionManager |
| Flatpak | fine-grained | --talk-name=org.gnome.SessionManager.Presence |
| Flatpak | fine-grained | --talk-name=org.gnome.SettingsDaemon |
| Flatpak | fine-grained | --talk-name=org.gnome.SettingsDaemon.Color |
| Flatpak | fine-grained | --talk-name=org.gnome.SettingsDaemon.MediaKeys |
| Flatpak | fine-grained | --talk-name=org.gnome.Shell |
| Flatpak | fine-grained | --talk-name=org.gnome.Shell.Screenshot |
| Flatpak | fine-grained | --talk-name=org.gtk.Notifications |
| Flatpak | fine-grained | --talk-name=org.gtk.vfs |
| Flatpak | fine-grained | --talk-name=org.gtk.vfs.* |
| Flatpak | fine-grained | --talk-name=org.kde.JobViewServer |
| Flatpak | fine-grained | --talk-name=org.kde.kuiserver |
| Flatpak | fine-grained | --talk-name=org.kde.kwalletd |
| Flatpak | fine-grained | --talk-name=org.kde.kwalletd5 |
| Flatpak | fine-grained | --talk-name=org.kde.StatusNotifierWatcher |
| Flatpak | fine-grained | --talk-name=org.mate.SessionManager |
| Flatpak | fine-grained | --talk-name=org.mpris.MediaPlayer2.Player |
| Flatpak | fine-grained | --talk-name=org.wiimotedev.deviceEvents |
| Snap | fine-grained | browser-support |
| Snap | fine-grained | calendar-service |
| Snap | fine-grained | cifs-mount |
| Snap | fine-grained | contacts-service |
| Snap | fine-grained | content |
| Snap | fine-grained | dot-config-inkscape |
| Snap | fine-grained | dot-local-share-xorg-logs |
| Snap | fine-grained | gpg-keys |
| Snap | fine-grained | gsettings |
| Snap | fine-grained | log-observe |
| Snap | fine-grained | login-session-observe |
| Snap | fine-grained | media-hub |
| Snap | fine-grained | password-manager-service |
| Snap | fine-grained | screen-inhibit-control |
| Snap | fine-grained | screencast-legacy |
| Snap | fine-grained | ssh-keys |
| Snap | fine-grained | ssh-public-keys |


## System IPC Permission Group

| Ecosystem | Granularity | Permission |
| ---- | ---- | ---- |
| Flatpak | coarse-grained | --socket=system-bus |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.GeoClue2 |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.Avahi |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.login1 |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.UDisks2 |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.ColorManager |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.NetworkManager |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.fwupd |
| Flatpak | fine-grained | --system-talk-name=org.freedesktop.timedate1 |
| Snap | fine-grained | accounts-service |
| Snap | fine-grained | avahi-control |
| Snap | fine-grained | avahi-observe |
| Snap | fine-grained | fwupd |
| Snap | fine-grained | hostname-control |
| Snap | fine-grained | locale-control |
| Snap | fine-grained | location-observe |
| Snap | fine-grained | mount-observe |
| Snap | fine-grained | network-control |
| Snap | fine-grained | network-manager |
| Snap | fine-grained | network-manager-observe |
| Snap | fine-grained | network-observe |
| Snap | fine-grained | network-status |
| Snap | fine-grained | openvswitch |
| Snap | fine-grained | process-control |
| Snap | fine-grained | shutdown |
| Snap | fine-grained | system-observe |


