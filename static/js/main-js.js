/**
 * Created by Administrator on 2019-07-03.
 */
    //all所有页面必须执行的方法


    function cookiegetphone(key) {
    var cookiesList = document.cookie.split(";");
    for (i = 0; i < cookiesList.length; i++) {
        cookieskey = cookiesList[i].split("=");
        if ($.trim(cookieskey[0]) == key) {    /*去掉空格*/
            return cookieskey[1]
        }
    }
}
    //展示用户昵称

    function userName() {
        $(".userName").text(cookiegetphone("phone"))
    }


    function toast(a) {
        var fartherEle=$("body");
        var childEle=$("<div class='toast'></div>");

        var toastEle=$("<span class='toastText'></span>");


        childEle.appendTo(fartherEle);
        childEle.append(toastEle);
        $(".toastText").html(a)

    }
    
    function cleanToast() {
        setTimeout(function () {
            $('.toast').remove()
        },2000)
    }


    // function bingClik(ele) {
    //     console.log("执行了");
    //     $(ele).each(function (index,element) {
    //      console.log("111111");
    //     console.log(index) ;
    //      console.log(element);
    //      $(element).click(function () {
    //          var procode=$(element).parent().siblings().eq(0).html();
    //          console.log(procode)
    //      })
    //  });
    // }
    //





