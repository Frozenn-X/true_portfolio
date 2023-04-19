
$('.collapse').on('shown.bs.collapse', function () {
    $(this).parent().find('.text-collapse').text('En savoir moins -');
});
$('.collapse').on('hidden.bs.collapse', function () {
    $(this).parent().find('.text-collapse').text('En savoir plus +');
});