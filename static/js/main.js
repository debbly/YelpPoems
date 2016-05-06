function scrollBottom(){
    window.scrollTo(0,document.body.scrollHeight);
}

function getInput() {
	text = $("input").text();
	appendLine(text);
}

function appendLine(text) {
    $("#poetry").append(text + "<br>");
}

(function poll() {
    setTimeout(function() {
        $.ajax({
            url: "/line",
            type: "GET",
            success: function(text) {
                getInput();
            },
            dataType: "text",
            complete: poll,
            timeout: 2000
        })
    }, 500);
})();
