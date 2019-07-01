/**
 * Created by Administrator on 2019/6/29.
 */

    //判断字符串是否属于列表
        function inArray(a,b) {
        for (var  i  in  b){
            if(a==b[i]){
                return true
            }
        }
    }


    //给二级dd标签添加display=none 隐藏起来
    $('.left-one dl dd').addClass("active");

    $('.left-one dl dt').addClass('icon iconfont icon-menu-fill');
    $('.left-one dl dt span').addClass('icon iconfont icon-arrowBottom-fill');

    $('.left-one dt').click(function () {
        var cls=$(this).children('span').attr('class');
        console.log(cls)
        if (cls=="icon iconfont icon-arrowBottom-fill"){
            $(this).children('span').attr('class','icon iconfont icon-arrowTop-fill');
             $(this).siblings().removeClass("active")

        }else {
              $(this).children('span').attr('class','icon iconfont icon-arrowBottom-fill');
              $(this).siblings().addClass("active")
        }
    })



    //打开关闭左侧导航栏

    $('.openLeft').click(function () {
        var ElementOpenLeft=$(this).attr("class");
        var ElementList=ElementOpenLeft.split(" ");
        if (inArray("icon-icon-test5",ElementList)){
            var intCode=ElementList.indexOf("icon-icon-test5");
            ElementList[intCode]="icon-icon-test4";
            strElement=ElementList.join(" ");
            $(this).attr("class",strElement);

            $(".left").addClass("active");
            $('.right').css("margin-left","20px")

        }else {
            var intCode=ElementList.indexOf("icon-icon-test4");
            ElementList[intCode]="icon-icon-test5";
            strElement=ElementList.join(" ");
            $(this).attr("class",strElement);
            $(".left").removeClass("active");
             $('.right').css("margin-left","200px")
        }
    })

    //实时监控input方法

    function acceptInp(element) {
        $(element).on('input',function () {
            console.log($(element).val());
            var textInp=$(element).val();
        if(textInp==""){
            $(element).siblings().addClass("active")

        }else {
             $(element).siblings().removeClass("active")
        }
    })}

    //一键删除输入框内容
    function removeInp(removeEle,inpEle) {
        $(removeEle).click(function () {
            $(inpEle).val("");
            $(inpEle).siblings().addClass("active")
        })
    }


    //首页新增
    $('.inp-button').children().eq(1).click(function () {
        console.log($(".project-add").attr("value"));
        if($(".project-add").attr("value")=="0"){
           $(".project-add").attr("value","1");
            $(".project-add").removeClass("active");
            $(".project-add-1").removeClass("active")
        }else {
            $(".project-add").attr("value","0");
            $(".project-add").addClass("active");
            $(".project-add-1").addClass("active")
        }
    })



    //取消蒙层
    $(".project-add-1-false").click(function () {
          $(".project-add").attr("value","0");
            $(".project-add").addClass("active");
            $(".project-add-1").addClass("active")
    })






