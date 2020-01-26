$(document).ready(function () {
    $("#happy").click(function(){
        $("body").css({"background": "linear-gradient(120deg, #FF9A54 , #FFEA6B, #54FEFB, #E7B2FF, #89FFCB)",
            "background-size": "1000% 1000%",
                
            "-webkit-animation": "AnimationName 10s ease infinite",
            "animation": "AnimationName 10s ease infinite"})
      });
    }
)
$(document).ready(function () {
    $("#sad").click(function(){
        $("body").css({"background": "linear-gradient(120deg, #494487, #3C3175, #522A66, #3B1840, #230B21)",
            "background-size": "1000% 1000%",
                
            "-webkit-animation": "AnimationName 10s ease infinite",
            "animation": "AnimationName 10s ease infinite"})
      });
    }
)
$(document).ready(function () {
    $("#calm").click(function(){
        $("body").css({"background": "linear-gradient(120deg, #280F36, #632B6C, #C76C98, #F09F9C, #FDC2A2)",
            "background-size": "1000% 1000%",
                
            "-webkit-animation": "AnimationName 10s ease infinite",
            "animation": "AnimationName 10s ease infinite"})
      });
    }
)

function click(id){
    console.log(id);
    const http = new XMLHttpRequest();

    http.open("GET", "http://127.0.0.1:5000/?play=true?playlist=None?song_id=" + id);
    http.send()

    http.onload = () => console.log(http.responseText)
}

        

