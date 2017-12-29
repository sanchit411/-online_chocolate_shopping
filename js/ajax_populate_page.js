/*  We load the global array proj4_data once, then use it as needed
    to retrieve product information.

    
    Sanchit Arora
    CS545
    Fall 2017
*/    


var proj4_data;

$(document).ready(function() {
    proj4_data = new Array();
    $.get('/perl/jadrn003/get_products.cgi', storeData);

    var cart = new shopping_cart("jadrn003");
    $('#milk').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Milk chocolate") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button'  id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"' value=\"Add to Cart\">";
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })

    $('#dark').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Dark chocolate") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button'  id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">"
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
    $('#nuts').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Nuts and chews") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button' id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">"
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
    $('#brittle').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Brittles and toffies") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button' id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">"
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
    $('#truffles').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Truffles") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button' id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">";
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
    $('#gifts').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Gifts") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button' id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">"
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
    $('#holiday').on('click', function() {
        $('a').removeClass('active');
        $(this).addClass('active');
        tmpString = "";
        for(var i=0; i < proj4_data.length; i++) {
            if(proj4_data[i][1] == "Holiday assortments") {
                tmpString +="<div class='card card-size'>";
                tmpString += "<img class='img-thumbnail card-img-top' src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\""+
                " />";          
                tmpString += "<div class='card-body'>\n"+"<h4 class='card-title'>"+proj4_data[i][2]+"</h4>";
                tmpString += "<p class='card-text'>"+proj4_data[i][3]+"<br /><strong>$"+proj4_data[i][6]+"</strong></p>"
                tmpString += "<input class='btn btn-primary buy' type='button'  id='"+proj4_data[i][2]+"_"+proj4_data[i][6]+"' name='" + proj4_data[i][0]+"'value=\"Add to Cart\">"
                tmpString += "</div></div>";                
                }
            }
        var handle = document.getElementById('content');
        handle.innerHTML = tmpString;
        })
                                
       
    $('#content').on('click',$('input[type="button"]'), function(e) {
        if($(e.target).val() != 'Add to Cart') return;
        alert("The SKU is " + $(e.target).attr("name"));
    });
        
    $(document).on('click', ".buy", function() {  
        var sku = this.name;
        var pair = this.id.split("_");
        var title = pair[0];
        var price = pair[1];
        cart.add(sku,1,title,price);
        $(this).next().fadeIn(50).fadeOut(2000);
    });             
});    

    
function storeData(response) {
    var tmpArray = explodeArray(response,';');
    for(var i=0; i < tmpArray.length; i++) {
        innerArray = explodeArray(tmpArray[i],'|');
        proj4_data[i] = innerArray;
        }
    }


// from http://www.webmasterworld.com/forum91/3262.htm            
function explodeArray(item,delimiter) {
tempArray=new Array(1);
var Count=0;
var tempString=new String(item);

while (tempString.indexOf(delimiter)>0) {
tempArray[Count]=tempString.substr(0,tempString.indexOf(delimiter));
tempString=tempString.substr(tempString.indexOf(delimiter)+1,tempString.length-tempString.indexOf(delimiter)+1);
Count=Count+1
}

tempArray[Count]=tempString;
return tempArray;
}     