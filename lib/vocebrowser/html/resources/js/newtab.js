$(window).on('load', function() {
    $('#thanksModal').modal('show');
});
$(function() {
    $("#search").addClass("d-none");
});
$(".toggle-search").click(function() {
    $("#search").removeClass("d-none");
    $("#search").addClass("d-block slideDown");
    $(".navbar").removeClass("d-flex slideDown");
    $(".navbar").addClass("d-none");
});
$(".hide-search").click(function() {
    $("#search").removeClass("d-block slideDown");
    $(".navbar").addClass("d-flex slideDown");
    $("#search").addClass("d-none");
});