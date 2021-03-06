Name:           ipxe
Version:        1.0.0_f3c2da7
Release:        12
URL:            https://ipxe.org
Source0:        https://git.ipxe.org/ipxe.git/snapshot/1b67a0564657b6fcef18b1588ea6491ca1b1996d.tar.bz2
Summary:        Open source network boot firmware
Group:          kernel
License:        GPL-2.0
BuildRequires:  binutils-dev
BuildRequires:  xz-dev
BuildRequires:  zlib-dev
BuildRequires:  perl
Patch1:         5dce2d454b2829431e0484ac0f993b7a2759e0df.patch

%description
iPXE is the leading open source network boot firmware.
It provides a full PXE implementation enhanced with
additional features.

You can use iPXE to replace the existing PXE ROM on
your network card, or you can chainload into iPXE to
obtain the features of iPXE without the hassle of
reflashing. 

%prep
%setup -q -n ipxe-1b67a05
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
# otherwise the build fails with gcc 10...
export EXTRA_CFLAGS="-fcommon"

make -C src NO_WERROR=1 bin/undionly.kpxe
make -C src NO_WERROR=1 bin-i386-efi/ipxe.efi
make -C src NO_WERROR=1 bin-x86_64-efi/ipxe.efi


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/ipxe
cp src/bin/undionly.kpxe       %{buildroot}/usr/share/ipxe/undionly.kpxe 
cp src/bin-i386-efi/ipxe.efi   %{buildroot}/usr/share/ipxe/ipxe-i386.efi
cp src/bin-x86_64-efi/ipxe.efi %{buildroot}/usr/share/ipxe/ipxe-x86_64.efi

%files
%defattr(-,root,root,-)
%dir /usr/share/ipxe
/usr/share/ipxe/undionly.kpxe
/usr/share/ipxe/ipxe-i386.efi
/usr/share/ipxe/ipxe-x86_64.efi
%doc COPYING COPYING.GPLv2 COPYING.UBDL
