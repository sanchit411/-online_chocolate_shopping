#!/usr/bin/perl  

use CGI;
use DBI;
use CGI::Cookie;


print <<END_CONTENT;
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
        <!--link rel="stylesheet" type="text/css" href="style.css" /-->
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <!-- Website CSS style -->
            <link href="http://jadran.sdsu.edu/~jadrn003/proj4/bootstrap/css/bootstrap.min.css" rel="stylesheet">
            <link href="http://jadran.sdsu.edu/~jadrn003/proj4/css/style.css" rel="stylesheet">        
        <!-- Website Font style -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">   
        <!-- Google Fonts -->
            <link href='https://fonts.googleapis.com/css?family=Passion+One' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>
        <!-- JS Bootstrap -->
            <script type="text/javascript" src="http://jadran.sdsu.edu/~jadrn003/proj4/bootstrap/js/jquery.js"></script>
            <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.13.0/esm/popper.js"></script>
            <script type="text/javascript" src="http://jadran.sdsu.edu/~jadrn003/proj4/bootstrap/js/bootstrap.js"></script>

            
    </head>
    <body> 
      <nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
            <a class="navbar-brand" href="#">Chocolates</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-item nav-link " href="http://jadran.sdsu.edu/~jadrn003/proj4/index.html">Home</a>
                    <a class="nav-item nav-link" href="http://jadran.sdsu.edu/~jadrn003/proj4/product.html">Products</a>
                    <a class="nav-item nav-link" href="http://jadran.sdsu.edu/~jadrn003/proj4/order_online.html">Order Online</a>
                    <a class="nav-item nav-link" href="http://jadran.sdsu.edu/~jadrn003/proj4/about.html">About Us</a>
                    <a class="nav-item nav-link" href="http://jadran.sdsu.edu/~jadrn003/proj4/contact.html">Contact</a>
                </div>
            </div>
        </nav>

END_CONTENT


$q = new CGI;

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn003";
my $username = "jadrn003";
my $password = "potato";
my $database_source = "dbi:mysql:$database:$host:$port";


my $dbh = DBI->connect($database_source, $username, $password)
or die 'Cannot connect to db';
#send a blank cookie.  You must insert this into the header before
#printing anything.  Also, using the CGI module makes printing
#content-type: text/html redundant.



#send a blank cookie.  You must insert this into the header before
#printing anything.  Also, using the CGI module makes printing
#content-type: text/html redundant.

my $cookie = $q->cookie(-name=>'jadrn003',-value=>'',-path=>'/');
print $q->header(-cookie=>$cookie);

   
%cookies = CGI::Cookie->fetch;

$first_name = $q->param("first_name");
$credit_card = $q->param("credit_card");
$payment = $q->param("payment");
@num = split('-',$credit_card);

$num = @num[3];

$phone = $q->param("phone");

print "<h1>Thank $first_name, for shopping with us</h1>";

print <<BODY_CONTENT;

<div class="card">
    <div class="card-header text-center">Products</div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <td><strong>Item Name</strong></td>
                        <td class="text-center"><strong>Item Quantity</strong></td>
                    </tr>
                </thead>
                <tbody>
                    
BODY_CONTENT
 
my $v = $q->cookie('jadrn003');

@rows = split('\|\|',$v);
 my $statement = "";
 my $sth = $dbh->prepare($statement);
foreach $row (@rows) {
    ($sku, $qty, $name, $price) = split('\|',$row);
    $statement = "INSERT INTO sales (sku,quantity,date) VALUES('$sku','$qty',NOW());";
    $sth = $dbh->prepare($statement);
    $sth->execute();

    print "<tr><td class='text-left'>$name</td><td class='text-center'>$qty</td></tr>";
    } 
   
$sth->finish();
$dbh->disconnect();

print  "</tbody></table></div></div></div>";
     
print "<h1>The above products will be delivered in 3 days on the below shipping Address:</h1>\n";


print <<ADD_CONTENT;

<div class="card">
    <div class="card-header text-center">Shipping Address</div>
    <div class="card-body">
ADD_CONTENT

    print "<p class='confirmation'> ";
foreach $value ($q->param("shipping"))   {
    print "$value ";
}
print "Mobile : $phone";
print "</p>";
print "<h4> The payment was done using $payment card : XXXX-XXXX-XXXX-$num </h4>";


print "</div>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";

