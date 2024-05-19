$(document).ready(function(){
    $('#map_options_submission').keydown(function(e){
        if(e.which === 13){ // Check if the Enter key is pressed
            var filter = $("#filter-options").val();
            var inputValue; 
            if(filter == "nearby"){
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                        var latitude = position.coords.latitude;
                        var longitude = position.coords.longitude;
                        inputValue = `${latitude}:${longitude}`;
                        makeAjaxCall(inputValue, filter);
                    });
                } else {
                    console.log("Geolocation is not supported by this browser.");
                }
            }
            else{
                inputValue = $(this).val(); 
                console.log(inputValue)
                makeAjaxCall(inputValue, filter);
            }
        }
    });
});

function makeAjaxCall(inputValue, filter) {
    console.log(inputValue)
    $.ajax({
        url: "/trial",
        type: "POST",
        dataType: "json",
        data: {
            "place": inputValue,
            "filter": filter
        }, 
        success: function(data){
            console.log(data);
            var listingDiv = $(".listing_box");
            listingDiv.html("");
            for(let i = 0; i < data.text.length; i++){
                var newDiv = $('<div></div>').addClass('listing');
                var newParagraph = $('<p></p>');
                var newImage = $('<img>').addClass('station-logo').attr('src', "{{url_for('static', filename='images/Screenshot from 2024-04-10 17-29-31.png')}}");
                var span1 = $('<span></span>').text(data.text[i][0]);
                var span2 = $('<span></span>').text(data.text[i][1]);
                newParagraph.append(newImage, '<br>', span1, '<br>', span2);
                newDiv.append(newParagraph);
                var tooltip = $('<div></div>').addClass('additional-listing-info');
                var inner_tooltip_div = $('<div></div>').addClass('innerClass');
                var phone_para = $('<span></span>').text(`Phone Number: ${data.text[i][2]}`);
                var opening_hour_para = $('<span></span>').text(`Address: ${data.text[i][3]}`);
                var price_lists = $('<span></span>').text.text(`Prices: ${data.text[i][4]}`);
                inner_tooltip_div.append(phone_para, '<br>', opening_hour_para, '<br');
                tooltip.append(inner_tooltip_div);
                newDiv.append(tooltip)
                listingDiv.append(newDiv);
            }
        }
    });
}
