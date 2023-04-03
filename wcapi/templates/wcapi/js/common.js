$(function(){
	$('.create .fields .field .upload').click(function(){
		$('.create .fields .field input[type=file]').click();
	});
	$('.page-content .nav ul li a.with_sub').click(function() {
		$(this).toggleClass('opened');
		$(this).next('ul').slideToggle();
	});
	$('.page-content .nav .name').click(function() {
		$(this).toggleClass('active');
		$(this).next('.ul').slideToggle();
	});
});