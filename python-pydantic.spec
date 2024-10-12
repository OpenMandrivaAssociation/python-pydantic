Name:		python-pydantic
Version:	2.9.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydantic/pydantic-%{version}.tar.gz
Summary:	Data validation using Python type hints
URL:		https://pypi.org/project/pydantic/
License:	None
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildArch:	noarch

%description
Data validation using Python type hints

%prep
%autosetup -p1 -n pydantic-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pydantic
%{py_sitedir}/pydantic-*.*-info
