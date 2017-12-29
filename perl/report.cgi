#!/usr/bin/perl  

use CGI;
use DBI;


use File::Path;

print "Content-type: text/html\n\n";
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
        <div class="container">
        <table class='table table-bordered'>
        <thead >
            <tr>
            <td><strong>Item Name</strong></td> 
            <td class="text-center"><strong>Item Quantity</strong>
            </td><td class="text-center"><strong>Item Cost</strong>
            </td><td class="text-center"><strong>Actual Cost</strong></td>
            <td class="text-center"><strong>Profit</strong></td>

       </tr></thead><tbody>

END_CONTENT


my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn003";
my $username = "jadrn003";
my $password = "potato";
my $database_source = "dbi:mysql:$database:$host:$port";	
my $dbh = DBI->connect($database_source, $username, $password)
or die 'Cannot connect to db';

my $sth = $dbh->prepare("select proj4.products.title, jadrn003.sales.quantity, proj4.products.retail,  proj4.products.cost  from jadrn003.sales, proj4.products where jadrn003.sales.sku = proj4.products.sku  ORDER BY jadrn003.sales.sku");
$sth->execute();

$str = "";
$totalQuant = 0;
$totalaccounts = 0;
$totalCost = 0;
$localProfit = 0;
while(my @row=$sth->fetchrow_array()) {
print "<tr>\n";
		$totalQty += $row[1];
		$totalcost += ($row[1]*$row[2]);
		$totalActCost += ($row[1]*$row[3]);
        $localProfit = (($row[1]*$row[2])-($row[1]*$row[3]));

foreach $item (@row) { 
     print "<td class='text center'>$item</td>\n";  
  	 }         
      print "<td class='text center'>$localProfit</td>\n";
     print "</tr>\n"; 
}
 
$sth->finish();
$dbh->disconnect();
print "</tbody></table>";
my $profit = $totalcost - $totalActCost;

print "<p>Total quantity : $totalQty</p>";
print "<p>Total Cost :  \$ $totalcost</p>";
print "<p>Total Actual Cost :\$ $totalActCost</p>";
print "<p>Total profit : \$ $profit</p>";

print "</div>";
print "</body>";
print "</html>";