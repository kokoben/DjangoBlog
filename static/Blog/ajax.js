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
				document.getElementById(like_link).innerHTML = "Like";
				document.getElementById('like_'+json.post_id).innerHTML = (json.likes_count) + ' likes';
			}
			// if user hasn't liked the post.
			else{
				document.getElementById(like_link).innerHTML = "Unlike";
				document.getElementById('like_'+json.post_id).innerHTML = (json.likes_count + ' likes');
			}
		}
	});
	});
	});
