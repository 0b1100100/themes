$(function(e){
	$('.create .fields .field .upload').click(function(e){
		if(e.target.id == "preview_b"){
			$('#preview').click();
		}
		else if(e.target.id == "icons_b"){
			$('#icons').click();
		}
		else if(e.target.id == "wallpaper_b"){
			$('#wallpaper').click();
		}
		else if(e.target.id == "widgets_b"){
			$('#widgets').click();
		}
		else  {
			$('.create .fields .field input[type=file]').click();
		}
		$(window.console&&console.log(e.target.id));

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