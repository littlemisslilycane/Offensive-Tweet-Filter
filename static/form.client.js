(function () {
    var $inputfield, $funnybtn , $oppositebtn;
    var $span;



    $(main);
    function generatefunny() {
    tweet= $inputfield.val();
    var requestOptions = {
  method: 'POST',
  redirect: 'follow'
        };
  secretKey = "yhgsd568isugfus76sdfgjs767utyyjfv"
  tweet = encodeURI(tweet)
   if(tweet.includes("#")){
   tweet= tweet.replace("#","yhgsd568isugfus76sdfgjs767utyyjfv")
  }
fetch("http://127.0.0.1:5000/?tweet="+tweet+"&action=Funny", requestOptions)
  .then((response) => response.json())
  .then((result)=>{

  if(result['tweet'].includes("yhgsd568isugfus76sdfgjs767utyyjfv")){
   result['tweet'] = result['tweet'].replace("yhgsd568isugfus76sdfgjs767utyyjfv","#")
  }
  $span.html("<label>"+result['tweet']+"</label>")
  })
   }

function generateopposite() {
    tweet= $inputfield.val();
    var requestOptions = {
  method: 'POST',
  redirect: 'follow'
        };

 secretKey = "yhgsd568isugfus76sdfgjs767utyyjfv"
  tweet = encodeURI(tweet)
   if(tweet.includes("#")){
   tweet= tweet.replace("#","yhgsd568isugfus76sdfgjs767utyyjfv")
  }
fetch("http://127.0.0.1:5000/?tweet="+tweet+"&action=Opposite", requestOptions)
  .then((response) => response.json())
  .then((result)=>{
  if(result['tweet'].includes("yhgsd568isugfus76sdfgjs767utyyjfv")){
   result['tweet'] = result['tweet'].replace("yhgsd568isugfus76sdfgjs767utyyjfv","#")
  }

  $span.html("<label>"+result['tweet']+"</label>")
  })
   }




    function main(){
    $inputfield = $('#txtinput');
    $funnybtn = $('#btnfunny');
    $span = $("#output");

     $oppositebtn = $('#btnopposite');
     $funnybtn.click(generatefunny);
     $oppositebtn.click(generateopposite);
    tweet = $inputfield.val()

}

    })();