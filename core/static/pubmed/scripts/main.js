!function(t){t.fn.filterValue=function(t){return this.filter(function(n,i){return i.value===t.toString()})}}(jQuery),$(function(){function t(){var t=r.reduce(function(t,n,i){var e=n.find("input[type=text]");return e.val()?++i:t},1);e.filterValue(t).click()}function n(t){var n=t.target.value;r.slice(0,n).map(function(t){t.show()}),r.slice(n).map(function(t){t.hide()})}var i=$("#entry-form"),e=i.find("input[type=radio][name=treatment]"),r=[i.find("#div_id_treatment_1"),i.find("#div_id_treatment_2"),i.find("#div_id_treatment_3"),i.find("#div_id_treatment_4"),i.find("#div_id_treatment_5")],d=i.find("select");e.change(n),d.select2({theme:"bootstrap"}),t()}),$(function(){var t=$("#entry-form"),n=t.find("div[data-form-column=True] > div").find("label.col-xs-4.col-md-3.col-lg-2","div.col-xs-8.col-md-9.col-lg-10");n.hide()});