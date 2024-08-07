$(document).ready(function() {
    $("DIV#toggle_header").click(function () {
        const act = $("header").hasClass("red");
        if (act) {
            $("header").removeClass("red").addClass("green");
        } else {
            $("header").removeClass("green").addClass("red");
        }
    });
});
