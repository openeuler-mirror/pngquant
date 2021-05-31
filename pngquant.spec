Name:           pngquant
Version:        2.12.5
Release:        3
Summary:        PNG quantitative tool for reducing the size of the image file
License:        GPLv3+
URL:            http://pngquant.org
Source0:        https://github.com/pornel/pngquant/archive/%{version}/pngquant-%{version}.tar.gz

BuildRequires:  libpng-devel >= 1.2.46-1 zlib-devel >= 1.2.3-1 lcms2-devel libimagequant-devel >= %{version} gcc
Requires:       libpng >= 1.2.46-1 zlib >= 1.2.3-1 libimagequant >= %{version}

%description
Pngquant converts a 24/32-bit RGBA PNG image into an 8-bit palette that retains the alpha channel. Such images
are compatible with all modern web browsers and can use compatibility settings to help reduce transparency in
Internet Explorer 6.

%package        help
Summary:        Documentation for pngquant

%description    help
This package provides documentation for pngquant.

%prep
%autosetup -n pngquant-%{version} -p1

%build
export CFLAGS="%{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC"
%configure --with-openmp --with-libimagequant
%make_build

%install
%make_install

%check
%make_build test

%files
%doc README.md CHANGELOG COPYRIGHT
%{_bindir}/%{name}

%files help
%{_mandir}/man1/%{name}.1*

%changelog
* Mon May 31 2021 huanghaitao <huanghaitao8@huawei.com> - 2.12.5-3
- Completing build dependencies

* Fri Dec 13 2019 fengbing <fengbing7@huawei.com> - 2.12.5-2
- Package init

