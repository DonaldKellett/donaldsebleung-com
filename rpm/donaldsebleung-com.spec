%global appname donaldsebleung-com
%global version 0.2.3

Name: %{appname}
Version: %{version}
Release: 1%{?dist}
Summary: My personal website reinstated, this time written in Spring
License: MIT
URL: https://github.com/DonaldKellett/%{appname}
Source0: https://github.com/DonaldKellett/%{appname}/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven
Requires: java-11-openjdk, openssl

%description
My personal website reinstated, this time written in Spring

%prep
%setup -q

%build
mvn package

%install
mkdir -p %{buildroot}/%{_datadir}/%{appname}
cp target/personal-website-0.0.1-SNAPSHOT.jar %{buildroot}/%{_datadir}/%{appname}/%{appname}-%{version}.jar
mkdir -p %{buildroot}/%{_sysconfdir}/%{appname}
echo "P@ssw0rd" > %{buildroot}/%{_sysconfdir}/%{appname}/passwd
chmod 600 %{buildroot}/%{_sysconfdir}/%{appname}/passwd
echo "keyalias" > %{buildroot}/%{_sysconfdir}/%{appname}/keyalias
mkdir -p %{buildroot}/%{_bindir}
cat > %{buildroot}/%{_bindir}/%{appname} << EOF
#!/bin/bash

print_usage() {
  echo "Usage: %{appname} [--version]"
}

miss_keycert() {
  echo "Missing key-certificate pair:"
  echo "%{_sysconfdir}/%{appname}/key.pem"
  echo "%{_sysconfdir}/%{appname}/cert.pem"
}

if [[ \$# -gt 1 ]]; then
  print_usage
  exit 1
fi

if [[ \$# -eq 0 ]]; then
  if [[ "\$(whoami)" != root ]]; then
    echo "%{appname} must be run as root when invoked with no arguments"
    exit 1
  fi
  test -f %{_sysconfdir}/%{appname}/key.pem
  if [[ \$? -ne 0 ]]; then
    miss_keycert
    exit 1
  fi
  test -f %{_sysconfdir}/%{appname}/cert.pem
  if [[ \$? -ne 0 ]]; then
    miss_keycert
    exit 1
  fi
  test -f %{_sysconfdir}/%{appname}/passwd
  if [[ \$? -ne 0 ]]; then
    echo "Missing password file %{_sysconfdir}/%{appname}/passwd"
    exit 1
  fi
  test -f %{_sysconfdir}/%{appname}/keyalias
  if [[ \$? -ne 0 ]]; then
    echo "Missing key alias file %{_sysconfdir}/%{appname}/keyalias"
    exit 1
  fi
  TMP_DIR=\$(mktemp -d)
  cat %{_sysconfdir}/%{appname}/key.pem %{_sysconfdir}/%{appname}/cert.pem > \$TMP_DIR/keycert.pem
  openssl pkcs12 -export -in \$TMP_DIR/keycert.pem -out \$TMP_DIR/keystore.pkcs12 -name \$(cat %{_sysconfdir}/%{appname}/keyalias) -noiter -nomaciter -passin pass:"\$(cat %{_sysconfdir}/%{appname}/passwd)" -passout pass:"\$(cat %{_sysconfdir}/%{appname}/passwd)"
  SPRING_PROFILES_ACTIVE=prod SERVER_SSL_KEY_STORE=file://\$TMP_DIR/keystore.pkcs12 SERVER_SSL_KEY_STORE_PASSWORD=\$(cat %{_sysconfdir}/%{appname}/passwd) SERVER_SSL_KEY_ALIAS=\$(cat %{_sysconfdir}/%{appname}/keyalias) java -jar %{_datadir}/%{appname}/%{appname}-%{version}.jar
  exit
fi

if [[ "\$1" == --version ]]; then
  echo "%{version}"
  exit
fi

print_usage
exit 1
EOF
chmod 755 %{buildroot}/%{_bindir}/%{appname}
mkdir -p %{buildroot}/usr/lib/systemd/system
cat > %{buildroot}/usr/lib/systemd/system/%{appname}.service << EOF
[Unit]
Description=My personal website reinstated, this time written in Spring

[Service]
ExecStart=%{_bindir}/%{appname}

[Install]
WantedBy=multi-user.target
EOF

%files
%{_datadir}/%{appname}/%{appname}-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{appname}/passwd
%config(noreplace) %{_sysconfdir}/%{appname}/keyalias
%{_bindir}/%{appname}
/usr/lib/systemd/system/%{appname}.service

%changelog
* Sun Mar 27 2022 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.2.3-1
- Update About and Qualifications pages to include CKA certification
* Fri Feb 25 2022 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.2.2-1
- Update About and Qualifications pages to include Alibaba Cloud certifications
- Fix typo "OpenFaas" to "OpenFaaS"
* Wed Jan 05 2022 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.2.1-1
- Update slogan on home page to reflect current conditions
- Add links to recent articles on cloud computing and associated resources
* Fri Dec 24 2021 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.2.0-1
- Update website content to include new qualifications and reflect changes in professional interest
* Sat Aug 28 2021 Donald Sebastian Leung <donaldsebleung@gmail.com> - 0.1.0-1
- Initial release
