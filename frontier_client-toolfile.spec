### RPM external frontier_client-toolfile 1.0
Requires: frontier_client
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/frontier_client.xml
<tool name="frontier_client" version="@TOOL_VERSION@">
  <lib name="frontier_client"/>
  <client>
    <environment name="FRONTIER_CLIENT_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE" default="$FRONTIER_CLIENT_BASE/include"/>
    <environment name="LIBDIR" default="$FRONTIER_CLIENT_BASE/lib"/>
  </client>
  <runtime name="FRONTIER_CLIENT" value="$FRONTIER_CLIENT_BASE/"/>
  <use name="zlib"/>
  <use name="openssl"/>
  <use name="expat"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
