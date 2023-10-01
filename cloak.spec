Name:           cloak
Version:        0.3.0
Release:        1
URL:            https://github.com/evansmurithi/cloak
Source0:        https://github.com/evansmurithi/cloak/archive/refs/heads/master.tar.gz
Summary:        A Command Line OTP Authenticator application.
License:        MIT
BuildRequires:  rustc
 
%description
A Command Line OTP Authenticator application.
    
%prep
%setup -q -n cloak-master
cargo fetch --locked
echo -e "[profile.release]\nlto = true\nincremental = false" >> Cargo.toml

%build
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --release --locked --offline


%install
install -D -m755 target/release/cloak %{buildroot}/usr/bin/cloak
strip --strip-debug %{buildroot}/usr/bin/cloak

%files
%defattr(-,root,root,-)
/usr/bin/cloak
