### RPM external hwloc 1.11.3

Source: https://www.open-mpi.org/software/hwloc/v1.11/downloads/%{n}-%{realversion}.tar.gz

Provides: libnuma.so.1()(64bit)
Provides: libnuma.so.1(libnuma_1.1)(64bit)
Provides: libnuma.so.1(libnuma_1.2)(64bit)
Provides: libcairo.so.2()(64bit)

%prep
%setup  -n %{n}-%{realversion}

%build
./configure --prefix=%{i}

make -j8

%install
make install

