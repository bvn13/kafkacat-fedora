Name: kafkacat
Version: 1.6.0
Release: 1%{?dist}
Summary: kafkacat is a generic non-JVM producer and consumer for Apache Kafka 0.8, think of it as a netcat for Kafka.

License:  BSD-2-Clause
URL:      https://github.com/edenhill/kafkacat

Source0:  %{version}.zip

Source:   https://github.com/edenhill/kafkacat/archive/refs/tags/1.6.0.zip

BuildRequires: zlib-devel
BuildRequires: gcc >= 4.1
BuildRequires: librdkafka-devel

%description
kafkacat is a generic non-JVM producer and consumer for Apache Kafka

%prep
%autosetup

%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/kafkacat

%doc README.md
%license LICENSE
%changelog CHANGELOG.md
