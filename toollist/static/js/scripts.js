$(document).ready(function() {
	$('.trigger_comment').on('click', function() {
		var next = $(this).next();
		
		if (next.hasClass('comment_show')) {
			next.removeClass('comment_show');
		} else {
			$('.comment_show').removeClass('comment_show');
			next.addClass('comment_show');
		}
	});
});
