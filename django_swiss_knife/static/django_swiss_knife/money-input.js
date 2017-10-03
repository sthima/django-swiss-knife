(function ($) {
  // TODO (mmarchini) set currency
  // TODO (mmarchini) make it work with dynamically loaded fields
  $("[data-money-field]").mask("#.##0,00", {reverse: true});
})(django.jQuery);
