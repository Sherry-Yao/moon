function submit() {
    $(".next").attr("src", "/static/img/next_press.png");
    $("#myform").submit();
}

function replay() {
    $(".again").attr("src", "/static/img/again_press.png");
}

function begin() {
    $(".begin").attr("src", "/static/img/begin_press.png");
}

window.onload = function() {
    //$(".bg").attr("width", "100%");
    //$(".view").css("width", window.screen.width);
    var len = $(".show").length;
    for (var i = 0; i < len; i++) {
        var w = $(".view").find(".show").eq(i).find("img").css("width");
        if (typeof(w) != "undefined") {
            var w_len = parseInt(w.substr(0, w.length - 2));
            $(".view").find(".show").eq(i).find("img").attr("width", w_len * document.body.clientWidth / 700 + 'px');
        }
	}
    if (window.screen.height > 500) {
		$(".begin").css("margin-top", "10%");
        $(".again").css("margin-top", "50%");
	} else {
		$(".begin").css("margin-top", "5%");
        $(".again").css("margin-top", "15%");
	}
	if (typeof($("#q_text").css("height")) != "undefined") {
        var q_text_h = parseInt($("#q_text").css("height").substr(0, $("#q_text").css("height").length - 2) * 1.3);
		if (q_text_h > 200) {
		    $(".frame").attr("height", q_text_h);
			$("#q_text").css("margin-top", -q_text_h * 0.9);
		} else {
			$(".frame").attr("height", q_text_h * 1.2);
			$("#q_text").css("margin-top", -q_text_h);
		}
    }
};
