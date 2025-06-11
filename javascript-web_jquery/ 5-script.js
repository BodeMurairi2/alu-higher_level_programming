// add li element to a list when add_item is clicked

$(document).ready(function () {
    $("#add_item").click(function () {
        $(".my_list").append("<li>Item</li>");
    });
});
