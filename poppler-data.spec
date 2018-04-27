#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : poppler-data
Version  : 0.4.9
Release  : 2
URL      : https://poppler.freedesktop.org/poppler-data-0.4.9.tar.gz
Source0  : https://poppler.freedesktop.org/poppler-data-0.4.9.tar.gz
Summary  : Encoding files for use with poppler
Group    : Development/Tools
License  : GPL-2.0
Requires: poppler-data-data
BuildRequires : cmake

%description
poppler-data
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them
if they are present.  When installed, the encoding files enables
poppler to correctly render CJK and Cyrrilic properly.  While poppler
is licensed under the GPL, these encoding files have different license,
and thus distributed separately.

%package data
Summary: data components for the poppler-data package.
Group: Data

%description data
data components for the poppler-data package.


%package dev
Summary: dev components for the poppler-data package.
Group: Development
Requires: poppler-data-data
Provides: poppler-data-devel

%description dev
dev components for the poppler-data package.


%prep
%setup -q -n poppler-data-0.4.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524864235
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1524864235
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-0
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-1
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-2
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-3
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-4
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-5
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-6
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-7
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-B5pc
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-ETen-B5
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-H-CID
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-H-Host
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-H-Mac
/usr/share/poppler/cMap/Adobe-CNS1/Adobe-CNS1-UCS2
/usr/share/poppler/cMap/Adobe-CNS1/B5-H
/usr/share/poppler/cMap/Adobe-CNS1/B5-V
/usr/share/poppler/cMap/Adobe-CNS1/B5pc-H
/usr/share/poppler/cMap/Adobe-CNS1/B5pc-UCS2
/usr/share/poppler/cMap/Adobe-CNS1/B5pc-UCS2C
/usr/share/poppler/cMap/Adobe-CNS1/B5pc-V
/usr/share/poppler/cMap/Adobe-CNS1/CNS-EUC-H
/usr/share/poppler/cMap/Adobe-CNS1/CNS-EUC-V
/usr/share/poppler/cMap/Adobe-CNS1/CNS1-H
/usr/share/poppler/cMap/Adobe-CNS1/CNS1-V
/usr/share/poppler/cMap/Adobe-CNS1/CNS2-H
/usr/share/poppler/cMap/Adobe-CNS1/CNS2-V
/usr/share/poppler/cMap/Adobe-CNS1/ETHK-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/ETHK-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/ETen-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/ETen-B5-UCS2
/usr/share/poppler/cMap/Adobe-CNS1/ETen-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/ETenms-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/ETenms-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKdla-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKdla-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKdlb-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKdlb-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKgccs-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKgccs-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKm314-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKm314-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKm471-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKm471-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/HKscs-B5-H
/usr/share/poppler/cMap/Adobe-CNS1/HKscs-B5-V
/usr/share/poppler/cMap/Adobe-CNS1/UCS2-B5pc
/usr/share/poppler/cMap/Adobe-CNS1/UCS2-ETen-B5
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UCS2-H
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UCS2-V
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF16-H
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF16-V
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF32-H
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF32-V
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF8-H
/usr/share/poppler/cMap/Adobe-CNS1/UniCNS-UTF8-V
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-0
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-1
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-2
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-3
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-4
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-5
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-GBK-EUC
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-GBpc-EUC
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-H-CID
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-H-Host
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-H-Mac
/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-UCS2
/usr/share/poppler/cMap/Adobe-GB1/GB-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GB-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/GB-H
/usr/share/poppler/cMap/Adobe-GB1/GB-V
/usr/share/poppler/cMap/Adobe-GB1/GBK-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GBK-EUC-UCS2
/usr/share/poppler/cMap/Adobe-GB1/GBK-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/GBK2K-H
/usr/share/poppler/cMap/Adobe-GB1/GBK2K-V
/usr/share/poppler/cMap/Adobe-GB1/GBKp-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GBKp-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/GBT-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GBT-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/GBT-H
/usr/share/poppler/cMap/Adobe-GB1/GBT-V
/usr/share/poppler/cMap/Adobe-GB1/GBTpc-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GBTpc-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/GBpc-EUC-H
/usr/share/poppler/cMap/Adobe-GB1/GBpc-EUC-UCS2
/usr/share/poppler/cMap/Adobe-GB1/GBpc-EUC-UCS2C
/usr/share/poppler/cMap/Adobe-GB1/GBpc-EUC-V
/usr/share/poppler/cMap/Adobe-GB1/UCS2-GBK-EUC
/usr/share/poppler/cMap/Adobe-GB1/UCS2-GBpc-EUC
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UCS2-H
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UCS2-V
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF16-H
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF16-V
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF32-H
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF32-V
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF8-H
/usr/share/poppler/cMap/Adobe-GB1/UniGB-UTF8-V
/usr/share/poppler/cMap/Adobe-Japan1/78-EUC-H
/usr/share/poppler/cMap/Adobe-Japan1/78-EUC-V
/usr/share/poppler/cMap/Adobe-Japan1/78-H
/usr/share/poppler/cMap/Adobe-Japan1/78-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/78-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/78-V
/usr/share/poppler/cMap/Adobe-Japan1/78ms-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/78ms-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/83pv-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/90ms-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/90ms-RKSJ-UCS2
/usr/share/poppler/cMap/Adobe-Japan1/90ms-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/90msp-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/90msp-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/90pv-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/90pv-RKSJ-UCS2
/usr/share/poppler/cMap/Adobe-Japan1/90pv-RKSJ-UCS2C
/usr/share/poppler/cMap/Adobe-Japan1/90pv-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/Add-H
/usr/share/poppler/cMap/Adobe-Japan1/Add-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/Add-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/Add-V
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-0
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-1
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-2
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-3
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-4
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-5
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-6
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-90ms-RKSJ
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-90pv-RKSJ
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-H-CID
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-H-Host
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-H-Mac
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-PS-H
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-PS-V
/usr/share/poppler/cMap/Adobe-Japan1/Adobe-Japan1-UCS2
/usr/share/poppler/cMap/Adobe-Japan1/EUC-H
/usr/share/poppler/cMap/Adobe-Japan1/EUC-V
/usr/share/poppler/cMap/Adobe-Japan1/Ext-H
/usr/share/poppler/cMap/Adobe-Japan1/Ext-RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/Ext-RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/Ext-V
/usr/share/poppler/cMap/Adobe-Japan1/H
/usr/share/poppler/cMap/Adobe-Japan1/Hankaku
/usr/share/poppler/cMap/Adobe-Japan1/Hiragana
/usr/share/poppler/cMap/Adobe-Japan1/Hojo-EUC-H
/usr/share/poppler/cMap/Adobe-Japan1/Hojo-EUC-V
/usr/share/poppler/cMap/Adobe-Japan1/Hojo-H
/usr/share/poppler/cMap/Adobe-Japan1/Hojo-V
/usr/share/poppler/cMap/Adobe-Japan1/Katakana
/usr/share/poppler/cMap/Adobe-Japan1/NWP-H
/usr/share/poppler/cMap/Adobe-Japan1/NWP-V
/usr/share/poppler/cMap/Adobe-Japan1/RKSJ-H
/usr/share/poppler/cMap/Adobe-Japan1/RKSJ-V
/usr/share/poppler/cMap/Adobe-Japan1/Roman
/usr/share/poppler/cMap/Adobe-Japan1/UCS2-90ms-RKSJ
/usr/share/poppler/cMap/Adobe-Japan1/UCS2-90pv-RKSJ
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UCS2-H
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UCS2-V
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF16-H
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF16-V
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF32-H
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF32-V
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF8-H
/usr/share/poppler/cMap/Adobe-Japan1/UniHojo-UTF8-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UCS2-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UCS2-HW-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UCS2-HW-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UCS2-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF16-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF16-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF32-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF32-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF8-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS-UTF8-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF16-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF16-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF32-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF32-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF8-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJIS2004-UTF8-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJISPro-UCS2-HW-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJISPro-UCS2-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJISPro-UTF8-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJISX0213-UTF32-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJISX0213-UTF32-V
/usr/share/poppler/cMap/Adobe-Japan1/UniJISX02132004-UTF32-H
/usr/share/poppler/cMap/Adobe-Japan1/UniJISX02132004-UTF32-V
/usr/share/poppler/cMap/Adobe-Japan1/V
/usr/share/poppler/cMap/Adobe-Japan1/WP-Symbol
/usr/share/poppler/cMap/Adobe-Japan2/Adobe-Japan2-0
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-0
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-1
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-2
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-H-CID
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-H-Host
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-H-Mac
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-KSCms-UHC
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-KSCpc-EUC
/usr/share/poppler/cMap/Adobe-Korea1/Adobe-Korea1-UCS2
/usr/share/poppler/cMap/Adobe-Korea1/KSC-EUC-H
/usr/share/poppler/cMap/Adobe-Korea1/KSC-EUC-V
/usr/share/poppler/cMap/Adobe-Korea1/KSC-H
/usr/share/poppler/cMap/Adobe-Korea1/KSC-Johab-H
/usr/share/poppler/cMap/Adobe-Korea1/KSC-Johab-V
/usr/share/poppler/cMap/Adobe-Korea1/KSC-V
/usr/share/poppler/cMap/Adobe-Korea1/KSCms-UHC-H
/usr/share/poppler/cMap/Adobe-Korea1/KSCms-UHC-HW-H
/usr/share/poppler/cMap/Adobe-Korea1/KSCms-UHC-HW-V
/usr/share/poppler/cMap/Adobe-Korea1/KSCms-UHC-UCS2
/usr/share/poppler/cMap/Adobe-Korea1/KSCms-UHC-V
/usr/share/poppler/cMap/Adobe-Korea1/KSCpc-EUC-H
/usr/share/poppler/cMap/Adobe-Korea1/KSCpc-EUC-UCS2
/usr/share/poppler/cMap/Adobe-Korea1/KSCpc-EUC-UCS2C
/usr/share/poppler/cMap/Adobe-Korea1/KSCpc-EUC-V
/usr/share/poppler/cMap/Adobe-Korea1/UCS2-KSCms-UHC
/usr/share/poppler/cMap/Adobe-Korea1/UCS2-KSCpc-EUC
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UCS2-H
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UCS2-V
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF16-H
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF16-V
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF32-H
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF32-V
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF8-H
/usr/share/poppler/cMap/Adobe-Korea1/UniKS-UTF8-V
/usr/share/poppler/cidToUnicode/Adobe-CNS1
/usr/share/poppler/cidToUnicode/Adobe-GB1
/usr/share/poppler/cidToUnicode/Adobe-Japan1
/usr/share/poppler/cidToUnicode/Adobe-Korea1
/usr/share/poppler/nameToUnicode/Bulgarian
/usr/share/poppler/nameToUnicode/Greek
/usr/share/poppler/nameToUnicode/Thai
/usr/share/poppler/unicodeMap/Big5
/usr/share/poppler/unicodeMap/Big5ascii
/usr/share/poppler/unicodeMap/EUC-CN
/usr/share/poppler/unicodeMap/EUC-JP
/usr/share/poppler/unicodeMap/GBK
/usr/share/poppler/unicodeMap/ISO-2022-CN
/usr/share/poppler/unicodeMap/ISO-2022-JP
/usr/share/poppler/unicodeMap/ISO-2022-KR
/usr/share/poppler/unicodeMap/ISO-8859-6
/usr/share/poppler/unicodeMap/ISO-8859-7
/usr/share/poppler/unicodeMap/ISO-8859-8
/usr/share/poppler/unicodeMap/ISO-8859-9
/usr/share/poppler/unicodeMap/KOI8-R
/usr/share/poppler/unicodeMap/Latin2
/usr/share/poppler/unicodeMap/Shift-JIS
/usr/share/poppler/unicodeMap/TIS-620
/usr/share/poppler/unicodeMap/Windows-1255

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/poppler-data.pc
