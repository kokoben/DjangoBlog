$(document).ready(function(){
$('.like-link').click(function(e){
	e.preventDefault();
	// the url with specific user and post in regex.
	var href = $(this).attr('href');
	// the like button.
	var like_link = $(this).attr('id');

	$.ajax({
		url: href,
		success: function(json){
			// if user has already liked the post.
			if (json.liked === true){
				$('#like-link-'+json.post_id).html("Like");
				if (json.likes_count == 1){
					$('#like-'+json.post_id).html(json.likes_count + " like");
				}
				else{
					$('#like-'+json.post_id).html(json.likes_count + " likes");
				}
			}
			// if user hasn't liked the post.
			else{
				$('#like-link-'+json.post_id).html("Unlike");
				if (json.likes_count == 1){
					$('#like-'+json.post_id).html(json.likes_count + " like");
				}
				else{
					$('#like-'+json.post_id).html(json.likes_count + " likes");
				}
			}
		}
	});
});
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function jsonEscape(str){
	return str.replace(/\\n/g, "<br>");	
}


$(document).ready(function(){
$('#comment-form').submit(function(e){
	e.preventDefault();
	console.log("form submitted");
	$.ajax({
		type: "POST",
		url:  "/" + user + "/posts/" + post_number + "/",
		data: {the_comment: $('#comment-text').val() } ,
		success: function(json){
			var comment = JSON.stringify(json);
			comment2 = jsonEscape(comment);
			comment3 = JSON.parse(comment2);
			console.log(comment);
			console.log(comment2);
			console.log(comment3);
			console.log("Successful ajax");
			$('#comment-text').val('');
			var str = '<div class="comment">Posted by ' + json.user + " on " + comment3.comment + '</div>';
			document.getElementById("comment-section").innerHTML += str;
		}
	});
});
});

