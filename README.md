My personal website reinstated, this time written in Spring

## Installing

### With Homebrew

Applicable to macOS and Linux

macOS users, here is your chance to contribute by [testing the formula](https://github.com/DonaldKellett/homebrew-misc/issues/2) ;-)

Ensure [Homebrew](https://brew.sh) is installed on your system and up to date, then add the DonaldKellett/misc tap and install the formula donaldsebleung-com:

```bash
$ brew tap DonaldKellett/misc
$ brew install donaldsebleung-com
```

Next, run the following commands to make your CA-issued (or self-signed) key-certificate pair available to `donaldsebleung-com`:

```bash
$ donaldsebleung-com install-key < /path/to/your/key.pem
$ donaldsebleung-com install-cert < /path/to/your/cert.pem
```

If your private key is protected by a passphrase `<passphrase>`, run the following command to make `donaldsebleung-com` aware of it:

```bash
$ donaldsebleung-com set-passwd "<passphrase>"
```

Finally, invoke the start-service command as root to spin up the HTTPS server which can be accessed through https://localhost :

```bash
$ sudo donaldsebleung-com start-service
```

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
$ sudo donaldsebleung-com set-passwd "<passphrase>"
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

### From source

Applicable to any OS platform supporting Java 8 or later

Ensure that Java 8 or later is installed (ideally Java 11 or later) and that the `JAVA_HOME` variable is set correctly. Furthermore, ensure Git is installed. Then, in a terminal or command prompt:

```bash
$ git clone https://github.com/DonaldKellett/donaldsebleung-com.git
$ cd donaldsebleung-com
```

Now you can run the project with (replace `mvnw` with `mvnw.cmd` if on Windows):

```bash
$ ./mvnw spring-boot:run
```

Point your browser to https://localhost:8443 to see the result. Note that your browser may block the site due to the use of a self-signed certificate. In this case, it should be safe to ignore the warning and proceed with visiting the site.

Alternatively, you could package the project with (again, replace `mvnw` with `mvnw.cmd` if on Windows):

```bash
$ ./mvnw package
```

This creates a Java archive at `target/personal-website-0.0.1-SNAPSHOT.jar` which can be run with:

```bash
$ java -jar target/personal-website-0.0.1-SNAPSHOT.jar
```

For convenience, you may wish to move the JAR elsewhere.

## Credits

The front-end design is based on [Hyperspace](https://html5up.net/hyperspace) by [HTML5 UP](https://html5up.net), released under the [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

## License

[MIT](./LICENSE)
