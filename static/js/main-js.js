/**
 * Created by Administrator on 2019-07-03.
 */
    //all所有页面必须执行的方法
    function cookiegetphone(key) {

    var cookiesList = document.cookie.split(";");
    for (i = 0; i < cookiesList.length; i++) {
        console.log(i)
        cookieskey = cookiesList[i].split("=");
        if (cookieskey[0] == key) {
            return cookieskey[1]
        }
    }
}
    //展示用户昵称

    function userName() {
        $(".userName").text(cookiegetphone("phone"))
    }
