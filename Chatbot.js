const scriptName = "Test";
const IP = "http://192.168.0.6:3004/"

var PositionState = ['',0]
var replyFlag = false

const SIGNAL = ['진입신호', '지닙신호']
const POSITION = ['포지션', '포제션', '퐂지션']
const ENTERPRICE = ['진입가격','지닙가격']
const REVERAGE = ['배율','레버리지']
const STOPLOSS = ['손절가','솔절가']
const WAIT = ['진입 대기']
const CLEAR = ['청산']

var compareString = ""

function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {


  if(sender == "김성진" && msg == "ON") replyFlag = true
  else if(sender == "김성진" && msg == "OFF") replyFlag = false

  if(sender != '조준호' && sender != '전문가' && sender != '김성진'){
    Api.markAsRead(room);
  }
  else {
    msg = regExp(msg).replace(' ','') // 특수문자들 모두 제거
    var data
  
    if(isContain(msg, SIGNAL)){
  
      var result = "/"
      
      if(isContain(msg,['\n'])) data = msg.split('\n')
  
      var i;
      
      for(i = 0; i < data.length; i++){
        if(isContain(data[i],POSITION)) {
          result = result + (data[i].split(compareString)[1] + "/")
          //replier.reply('조준호',compareString)
          compareString = ""
        }
      }
  
      for(i = 0; i < data.length; i++){
        if(isContain(data[i],ENTERPRICE)){
          result = result + (data[i].split(compareString)[1] + "/")
          //replier.reply('조준호',compareString)
          compareString = ""
        } 
      }    
  
      for(i = 0; i < data.length; i++){
        if(isContain(data[i],REVERAGE)) {
          result = result + (data[i].split(compareString)[1] + "/")
          //replier.reply('조준호',compareString)
          compareString = ""
        }
      }
  
      PositionState = toServer(result, '진입신호')
      
      if(replyFlag) replier.reply(room,"1")
    }
    else if(isContain(msg, STOPLOSS)){
  
      var result = msg.replace(/[^0-9]/g, "");   // 원래 문자열에서 숫자가 아닌 모든 문자열을 빈 문자로 변경

      if(result.length > 0){
        if(PositionState[0].toLowerCase() == 'long'){
          if(PositionState[1] > Number(result)){
            toServer(result, '손절가')
            PositionState[0] = ''
            PositionState[1] = 0
          }
        }
        else{
          if(PositionState[1] < Number(result)){
            toServer(result, '손절가')
            PositionState[0] = ''
            PositionState[1] = 0
          }
        }
      }
    }
    else if(isContain(msg,WAIT)){
  
      var result = "진입대기"
      // toServer(result, '진입대기')
      replier.reply('김성진','진입대기')
    }
    else if(isContain(msg, CLEAR)){
      var result = "청산"
      PositionState[0] = ''
      PositionState[1] = 0
      
      toServer(result, '청산')  
    }
  }
}

function toServer(DATA, index){
  if(index == '진입신호') {

    while(isContain(DATA,[' '])){
      DATA = DATA.replace(' ','')
    }

    var temp = DATA.split('/')
    
    var test = "{" + '"position": '+'"'+temp[1]+'"'+',"raverage": '+'"'+temp[3].replace(/[^0-9]/g, "")+'"'+',"price": '+'"'+temp[2].replace(/[^0-9]/g, "")+'"'+"}"
    
    var res = org.jsoup.Jsoup.connect(IP+'enterPos')  //요청 주소
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .ignoreContentType(true)
    .ignoreHttpErrors(true)
    .requestBody(test)
    .post().text();
    
    return [temp[1], Number(temp[2].replace(/[^0-9]/g, ""))];
  }
  else if(index == '손절가'){
    var res = org.jsoup.Jsoup.connect(IP+'setStopLoss')  //요청 주소
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .ignoreContentType(true)
    .ignoreHttpErrors(true)
    .requestBody('{"price": "' + DATA + '"}')
    .post().text();
  }
  else if(index == '진입대기'){
    var res = org.jsoup.Jsoup.connect(IP+'waitpos')  //요청 주소
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .ignoreContentType(true)
    .ignoreHttpErrors(true)
    .requestBody('{}')
    .post().text();
  }
  else if(index == '청산'){
    var res = org.jsoup.Jsoup.connect(IP+'clear')  //요청 주소
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .ignoreContentType(true)
    .ignoreHttpErrors(true)
    .requestBody('{}')
    .post().text();
  }

}

function isContain(Data, Value){

  for(var i = 0 ; i < Value.length; i++){
    var check = Data.indexOf(Value[i])

    if(check != -1) {
      compareString = Value[i]
      return true
    }  
  }

  return false
}

function regExp(str){  
  var reg = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/gi

  if(reg.test(str)) return str.replace(reg, "");    
  else return str;
}

//아래 4개의 메소드는 액티비티 화면을 수정할때 사용됩니다.
function onCreate(savedInstanceState, activity) {
  var textView = new android.widget.TextView(activity);
  textView.setText("Hello, World!");
  textView.setTextColor(android.graphics.Color.DKGRAY);
  activity.setContentView(textView);
}

function onStart(activity) {}

function onResume(activity) {}

function onPause(activity) {}

function onStop(activity) {}