Name:		python-pydantic
Version:	2.12.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydantic/pydantic-%{version}.tar.gz
Summary:	Data validation using Python type hints
URL:		https://pypi.org/project/pydantic/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Data validation using Python type hints

%files
%{py_sitedir}/pydantic
%{py_sitedir}/pydantic-*.*-info
