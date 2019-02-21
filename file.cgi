#! C:/xampp/perl/bin/perl
# use strict;
use warnings;
use utf8;
binmode STDIN, ':encoding(cp932)';
binmode STDOUT, ':encoding(cp932)';
binmode STDERR, ':encoding(cp932)';

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD><TITLE>社員年齢分布りすと（その２）</TITLE></HEAD>\n";
print "<BODY>\n";

print "<H1>社員年齢分布リスト（その２）</H1><HR>\n";

if( open ( FH, "nenrei.dat")){

# @list = <FH>;
# close(FH);


foreach $fid (<FH>){
	chomp($fid);
	$syukei{$fid}++;
}
close(FH);

print "<TABLE border=1>\n";
print "<TR><TH>年齢</TH><TH>人数</TH></TR>\n";

foreach $key (reverse(sort(keys(%syukei)))) {
	$cut = $syukei{$key};
	print "<TR><TH>${key}才</TH><TH>${cut}人</TH></TR>\n";
}

print "</TABLE>\n";
}
else{
	print "ファイルオープンに失敗しました。 \n";
}
print "</BODY>\n";
print "</HTML>\n";

__END__