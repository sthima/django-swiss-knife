$(".selectAll").click(function(){
    $(this).parent().siblings().find('input').prop('checked', $(this).prop('checked'));
})
