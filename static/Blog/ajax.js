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

// when user submits comment form.
$(document).ready(function(){
$('#comment-form').on('submit', function(e){
	e.preventDefault();
	$.ajax({
		type: "POST",
		url:  "/" + user + "/posts/" + post_number + "/",
		data: {the_comment: $('#comment-text').val() } ,
		success: function(json){
			// append the comment.
			var parsed_json = JSON.stringify(json);
			parsed_json = jsonEscape(parsed_json);
			parsed_json = JSON.parse(parsed_json);
			// make comment textarea blank after submitting.
			$('#comment-text').val('');
			// generate the reply link address.
			var str = '<div class="comment">Posted by ' + json.user + " on " + parsed_json.comment + "<a href=/comments/reply/" + logged_in_user + "/" + post_number + "/" + json.comment_id + " class='reply-link' id='reply-link-" + json.comment_id + "'>Reply</a><div id='reply-form-section-" + json.comment_id + "'></div></div>";
			$('#comment-section').append(str);

			// increase the comment text count.
			if (json.comment_count == 1){
				$('#comment-count').html(json.comment_count + ' Comment:');
				}
			else
				$('#comment-count').html(json.comment_count + ' Comments:');
			}
		});
	});
});

// when user clicks on reply link.
$(document).ready(function(){
	$('#comment-section').on('click', '.reply-link', function(e){
		e.preventDefault();
		var href = $(this).attr('href');
		var default_link_color  = $('a').css('color');

		$.ajax({
			url: href,
			success: function(json){
				var reply_link = $('#reply-link-'+json.comment_id);
				// if reply link is same color as default link color, change to "selected" color.
				if (reply_link.css('color') == default_link_color){
					reply_link.css('color', 'yellow');
					color = reply_link.css('color');
					// then change any other selected, yellow reply link back to default color. (happens if another reply link was previously selected.
					for (i = 0; i < json.num_comments; i++){
						if (json.comments_list[i].id != json.comment_id){
							var non_reply_link = $('#reply-link-'+json.comments_list[i].id);
							if (non_reply_link.css('color') == color){
								non_reply_link.css('color', default_link_color);
								// also, hide its reply form.
								$('#reply-form-section-'+json.comments_list[i].id).empty();
							}
						}
					}
					var reply_link_on_success
					var str = "<form method='post'"
								+ " id='reply-form'>"
								+ csrf_token
								+ '<table>'
								+ reply_form
								+ '</table>'
								+ '<input type="submit", value="Reply!">'
								+ '</form>';
					$('#reply-form-section-'+json.comment_id).html(str);
				}
				// else, change it back to default color.
				else{
					reply_link.css('color', default_link_color);
					// also, hide the reply form again.
					$('#reply-form-section-'+json.comment_id).empty();
				}
			}
		});
	});
});

// when user submits reply form.
$(document).ready(function(){
	$('#reply-form').on('submit', (function(e){
		console.log("pupsdkl;fjkasl;fjaksl;fjkasl;fjk;aslfjAL:SKJDA:LDJEKL:SJDpies");
		e.preventDefault();
		console.log($('#reply-text').value());
		$.ajax({
			url: blah,
			data: {the_reply: $('#reply-text').value()},
			success: function(json){
				console.log("poop");
			}
		});
	}));
});


