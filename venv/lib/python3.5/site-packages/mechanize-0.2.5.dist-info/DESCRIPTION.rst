Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

mechanize.Browser implements the urllib2.OpenerDirector interface.  Browser
objects have state, including navigation history, HTML form state, cookies,
etc.  The set of features and URL schemes handled by Browser objects is
configurable.  The library also provides an API that is mostly compatible with
urllib2: your urllib2 program will likely still work if you replace "urllib2"
with "mechanize" everywhere.

Features include: ftp:, http: and file: URL schemes, browser history, hyperlink
and HTML form support, HTTP cookies, HTTP-EQUIV and Refresh, Referer [sic]
header, robots.txt, redirections, proxies, and Basic and Digest HTTP
authentication.

Much of the code originally derived from Perl code by Gisle Aas (libwww-perl),
Johnny Lee (MSIE Cookie support) and last but not least Andy Lester
(WWW::Mechanize).  urllib2 was written by Jeremy Hylton.



