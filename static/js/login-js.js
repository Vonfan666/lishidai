/**
 * Created by Administrator on 2019-06-26.
 */
    // 返回字段不会空则给出提示



    function errorMessage(a) {
       if(a!='null'){
        $('.error').removeClass('active')
    }
    }
        //点击输入框提示消失
    function deleteErrorMessage(a) {
        $(a).click(function () {
            $('.error').addClass('active')
        })
    }

    // 输入框聚焦
    function eventCommission(a,b) {
        $(a).click(function () {
            $(this).children('input').focus()
        })
    }



