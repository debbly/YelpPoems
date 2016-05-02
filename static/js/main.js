function scrollBottom(){
    window.scrollTo(0,document.body.scrollHeight);
}

function getInput() {
	$().text();
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
                getInput(text);
            },
            dataType: "text",
            complete: poll,
            timeout: 2000
        })
    }, 500);
})();
