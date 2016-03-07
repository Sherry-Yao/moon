function checkinput() {
	var len = $(".answer").length;
	for (var i = 0; i < len; i++) {
		if ($(".answer")[i].checked == true) {
			return true;
		}
	}
	layer.msg('还没有选答案哦！');
	$(".next").attr("src", "/static/img/next.png");
	return false;
}