%define module pydantic

Name:		python-pydantic
Version:	2.13.2
Release:	1
Summary:	Data validation using Python type hints
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pydantic
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Data validation using Python type hints

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
