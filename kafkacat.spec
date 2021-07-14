Name: kafkacat
Version: 1.7.0
Release: 1%(?dist)
Summary: kafkacat is a generic non-JVM producer and consumer for Apache Kafka 0.8, think of it as a netcat for Kafka.

Group:    Productivity/Networking/Other
License:  BSD-2-Clause
URL:      https://github.com/edenhill/kafkacat
Source:   kafkacat-%{version}.tar
Requires: librdkafka

BuildRequires: zlib-devel gcc >= 4.1 librdkafka-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
kafkacat is a generic non-JVM producer and consumer for Apache Kafka >= 0.8,
think of it as a netcat for Kafka.

In producer mode kafkacat reads messages from stdin, delimited with a
configurable delimeter (-D, defaults to newline), and produces them to the
provided Kafka cluster (-b), topic (-t) and partition (-p).

In consumer mode kafkacat reads messages from a topic and partition and prints
them to stdout using the configured message delimiter.

kafkacat also features a Metadata list (-L) mode to display the current state
of the Kafka cluster and its topics and partitions.

kafkacat is fast and lightweight; statically linked it is no more than 150Kb.

%prep
%setup -q

%configure
#./configure
./configure --prefix=/usr

%build
make

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(755,root,root)
%{_bindir}/kafkacat
%defattr(644,root,root)
%doc README.md
%doc LICENSE

