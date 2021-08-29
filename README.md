My personal website reinstated, this time written in Spring

## Installing

### From the Snap store

Applicable to Ubuntu and many other Linux distributions

Ensure `snapd` is [installed on your system](https://snapcraft.io/docs/installing-snapd), then install `donaldsebleung-com` [from the Snap store](https://snapcraft.io/donaldsebleung-com).

Next, run the following commands to make your CA-issued (or self-signed) key-certificate pair available to `donaldsebleung-com`:

```bash
$ sudo donaldsebleung-com install-key < /path/to/your/key.pem
$ sudo donaldsebleung-com install-cert < /path/to/your/cert.pem
```

If your private key is protected by a passphrase `<passphrase>`, run the following command to make `donaldsebleung-com` aware of it:

```bash
$ sudo donaldsebleung-com set-passwd <passphrase>
```

Finally, enable the service `snap.donaldsebleung-com.donaldsebleung-comd.service` to run at boot:

```bash
$ sudo systemctl enable --now snap.donaldsebleung-com.donaldsebleung-comd.service
```

### From Fedora COPR

Applicable to:

- Fedora 33
- Fedora 34
- Fedora 35
- Fedora Rawhide

Enable the `donaldsebleung/misc` repo and install the package `donaldsebleung-com`:

```bash
$ sudo dnf copr enable donaldsebleung/misc
$ sudo dnf install donaldsebleung-com
```

Then install the CA-issued key-certificate pair to their respective locations (or generate your own):

- `/etc/donaldsebleung-com/key.pem`
- `/etc/donaldsebleung-com/cert.pem`

If your private key is protected by a passphrase, edit `/etc/donaldsebleung-com/passwd` accordingly to contain the correct passphrase, then enable the service `donaldsebleung-com.service` to run at boot:

```bash
$ sudo systemctl enable --now donaldsebleung-com.service
```

### From Ubuntu PPA

Applicable to:

- Ubuntu 20.04 LTS (Focal Fossa)
- Ubuntu 21.04 (Hirsute Hippo)
- Ubuntu 21.10 (Impish Idri)

Add the `ppa:donaldsebleung/misc` repo and install the package `donaldsebleung-com`:

```bash
$ sudo add-apt-repository ppa:donaldsebleung/misc
$ sudo apt install donaldsebleung-com
```

Then install the CA-issued key-certificate pair to their respective locations (or generate your own):

- `/etc/donaldsebleung-com/key.pem`
- `/etc/donaldsebleung-com/cert.pem`

If your private key is protected by a passphrase, edit `/etc/donaldsebleung-com/passwd` accordingly to contain the correct passphrase, then enable the service `donaldsebleung-com.service` to run at boot:

```bash
$ sudo systemctl enable --now donaldsebleung-com.service
```

## Credits

The front-end design is based on [Hyperspace](https://html5up.net/hyperspace) by [HTML5 UP](https://html5up.net), released under the [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

## License

[MIT](./LICENSE)
