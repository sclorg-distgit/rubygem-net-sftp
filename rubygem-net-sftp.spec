%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-sftp

Summary: A pure Ruby implementation of the SFTP client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT or LGPLv2
URL: https://github.com/net-ssh/net-sftp
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh) >= 2.6.5

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
# Tests require test/unit compatible framework
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
#BuildRequires: %{?scl_prefix_ror}rubygem(mocha)
#BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A pure Ruby implementation of the SFTP client protocol

%package        doc
Summary:        Documentation for %{pkg_name}
Group:          Documentation
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
# Missing test/unit
#ruby -Itest test/test_all.rb
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/Manifest
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/gem-public_cert.pem
%{gem_instdir}/net-sftp.gemspec
%doc %{gem_docdir}
# License: LGPL version 2.1
%{gem_instdir}/setup.rb

%changelog
* Mon Jun 08 2015 Josef Stribny <jstribny@redhat.com> - 2.1.2-4
- Disable tests as we lack test/unit in RHSCL

* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 2.1.2-3
- Add missing provide

* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 2.1.2-2
- Add SCL macros

* Tue Jul 15 2014 Vít Ondruch <vondruch@redhat.com> - 2.1.2-1
- Update to net-sftp 2.1.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 2.1.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to net-sftp 2.1.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.5-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Michal Fojtik <mfojtik@redhat.com> - 2.0.5-2
- Fixed license
- Fixes source0 URL

* Wed Oct 13 2010 Michal Fojtik <mfojtik@redhat.com> - 2.0.5-1
- Initial package
