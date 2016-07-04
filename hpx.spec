### RPM external hpx master

%define branch master
%define tag 400b232d1f1cb7fa8bf5649e5e1bb8d52134622f
Source: git+https://github.com/STEllAR-GROUP/%{n}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz

BuildRequires: cmake
Requires: boost jemalloc hwloc

%prep
%setup -q -n %{n}-%{realversion}

%build
mkdir hpx-build
cd hpx-build
cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_FLAGS=-std=c++11 \
  -DCMAKE_EXE_LINKER_FLAGS=-dynamic \
  -DCMAKE_INSTALL_PREFIX="%{i}" \
  -DHPX_WITH_MALLOC=JEMALLOC \
  -DJEMALLOC_INCLUDE_DIR:PATH=${JEMALLOC_ROOT}/include \
  -DJEMALLOC_LIBRARY:FILEPATH=${JEMALLOC_ROOT}/lib/libjemalloc.so \
  -DBOOST_ROOT=${BOOST_ROOT} \
  -DBoost_INCLUDE_DIR=${BOOST_ROOT}/include \
  -DBoost_LIBRARY_DIR=${BOOST_ROOT}/lib \
  -DHPX_WITH_TESTS:BOOL=ON \
  -DHPX_WITH_TESTS_BENCHMARKS=OFF \
  -DHPX_WITH_TESTS_EXTERNAL_BUILD=OFF \
  -DHPX_WITH_TESTS_HEADERS=OFF \
  -DHPX_WITH_TESTS_REGRESSIONS=OFF \
  -DHPX_WITH_EXAMPLES:BOOL=OFF \
  -DHPX_WITH_HWLOC:BOOL=ON \
  -DHWLOC_ROOT=${HWLOC_ROOT} \
  -DHWLOC_INCLUDE_DIR=${HWLOC_ROOT}/include \
  -DHWLOC_LIBRARY=${HWLOC_ROOT}/lib/libhwloc.so \
  -DHPX_WITH_PARCELPORT_MPI:BOOL=OFF \
  -DDART_TESTING_TIMEOUT=45 \
  ..

make -j4

%install
cd hpx-build
make install
