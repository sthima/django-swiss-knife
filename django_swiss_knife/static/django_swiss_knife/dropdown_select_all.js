$(".selectAll").click(function(){
    $(this).parent().parent().siblings().find('a').find('input').prop('checked', $(this).prop('checked'));
})
