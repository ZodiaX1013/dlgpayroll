// Progress Bar 

var elem = document.getElementById("progress-bar");
var width = 1;
var id = {};

function progressBar() {

  id = setInterval(frame, 10);

  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++;
      elem.style.width = width + '%'
      elem.innerHTML = width*1 + '%';
    }
  }
}

// ENd progressBar()

// Segment View

// "use strict";

// const body = document.body;
// const bgColorsBody = ["#ffb457", "#ff96bd", "#9999fb", "#ffe797", "#cffff1"];
// const menu = body.querySelector(".menu");
// const menuItems = menu.querySelectorAll(".menu__item");
// const menuBorder = menu.querySelector(".menu__border");
// let activeItem = menu.querySelector(".active");

// function clickItem(item, index) {
//   menu.style.removeProperty("--timeOut");

//   if (activeItem == item) return;

//   if (activeItem) {
//     activeItem.classList.remove("active");
//   }

//   item.classList.add("active");
//   body.style.backgroundColor = bgColorsBody[index];
//   activeItem = item;
//   offsetMenuBorder(activeItem, menuBorder);
// }

// function offsetMenuBorder(element, menuBorder) {
//   const offsetActiveItem = element.getBoundingClientRect();
//   const left =
//     Math.floor(
//       offsetActiveItem.left -
//         menu.offsetLeft -
//         (menuBorder.offsetWidth - offsetActiveItem.width) / 2
//     ) + "px";
// //   menuBorder.style.transform = `translate3d(${left}, 0 , 0)`;
// }

// offsetMenuBorder(activeItem, menuBorder);

// menuItems.forEach((item, index) => {
//   item.addEventListener("click", () => clickItem(item, index));
// });

// window.addEventListener("resize", () => {
//   offsetMenuBorder(activeItem, menuBorder);
//   menu.style.setProperty("--timeOut", "none");
// });

// Clear Function Of Form
function clearForm() {
  document.getElementById("employee").reset();
  // document.getElementById("emp2").reset();
  // document.getElementById("emp3").reset();
  // document.getElementById("emp4").reset();
}

function clearForm2() {
  // document.getElementById("eid").value = null
  // document.getElementById("pos").value = null
  // document.getElementById("lname").value = null
  // document.getElementById("fname").value = null
  document.getElementById("leave2").reset();
  
  // document.getElementById("emp").reset();
}

function clearForm3() {
  // document.getElementById("leave4").reset();
  document.getElementById("salary").reset();
  // document.getElementById("salary").reset();
  // document.getElementById("salary2").reset();
  // document.getElementById("salary3").reset();
  // document.getElementById("salary4").reset();
  // document.getElementById("salary5").reset();

  // document.getElementById("leave").reset();
  // document.getElementById("legal").reset();
  // document.getElementById("emp").reset();
}

// Save Button
function submitForms(){
  document.getElementById("emp").submit();
  // document.getElementById("emp2").submit();
  // document.getElementById("emp3").submit();
  // document.getElementById("emp4").submit();
}
function calculate()
// calculate = function()
{   
  // alert("Hello");
  
  // var temp, element = document.getElementById('efd')
  // if(element != null){
  //   str = element.value;
  //   alert(str)
  // }
  // else{
  //   alert("Null Value")
  // }
  var resources = document.getElementById('edf').value;
  var minutes = document.getElementById('month').value; 
  // alert(resources);
  // alert(minutes);
  // console.log(resources);
  // console.log(minutes);
  // document.getElementById('medf').value = parseFloat(resources) / parseFloat(minutes);
  document.getElementById('medf').value =Math.round(parseInt(resources)/parseInt(minutes));
     
}
// function disable()
// {
//   var radio = document.getElementById("optradiod3")
//   if(radio.value == "Yes"){
//     document.getElementById("lwork").disabled = true;
//     alert("In If")
//   }
//   else{
//     document.getElementById("lwork").disabled = false;
//     alert("In ELse")
//   }

//   // document.getElementById('custom').disabled = false; 
//   // document.getElementById('charstype').disabled = true;

//   // document.getElementById('custom').disabled = true; 
//   // document.getElementById('charstype').disabled = false;
// }

// Hire Date Must Be Before Last Working Day
function checkDate()
{
  var hire = document.getElementById('hire').value
  var last = document.getElementById('lwork').value

  // alert(hire)
  // alert(last)
  if(last < hire){
    // alert("In If")
    document.getElementById("lwork").value = "";
    // alert("After")
  }
  // alert("Out If")
}

// End DAte

// multi level selection list

var $select1 = $( '#dep' ),
		$select2 = $( '#sdep' ),
    $options = $select2.find( 'option' );
    
$select1.on( 'change', function() {
	$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

// end selection list

// set % to 100

function percentage(){
  var per = document.getElementById("per").value

  if(per > 100){
    document.getElementById("per").value = 100
  }
  else{
    document.getElementById("per").value = per
  }
}
// end perdentage

// Negative to Zero
function negativeCar(){
  var data = document.getElementById("car").value
  data = parseInt(data)
  if(data < 0){
    document.getElementById("car").value = 0
  }
  else{
    document.getElementById("car").value = data
  }
}

function negativeCar(){
  var data = document.getElementById("per").value
  data = parseInt(data)
  if(data < 0){
    document.getElementById("per").value = 0
  }
  else{
    document.getElementById("per").value = data
  }
}
// local and sick leave

function leave(){
  var local = document.getElementById("lleave").value
  var sick = document.getElementById("sleave").value

  if(local >365){
    document.getElementById("lleave").value = 365
  }
  else{
    document.getElementById("lleave").value = local
  }
  if(sick > 365){
    document.getElementById("sleave").value = 365
  }
  else{
    document.getElementById("sleave").value = sick
  }
}

// end leave

// Working Days

function days(){
  var days = document.getElementById("wday").value

  if(days > 30){
    document.getElementById("wday").value = 30
  }
  else{
    document.getElementById("wday").value = days
  }
}
//  End working

//  Next Employee ID

// function next(){
//   var emp = document.getElementById("eid")

// }

// end next

// Redirection Of Leave Page

function redirect() {
  let url = "http://127.0.0.1:5000/leave";
  window.location.href(url);
}

// End Of Redirection


function calculate2()
// calculate = function()
{   
  var edf = document.getElementById('edf').value;
  var month = document.getElementById('month').value; 
  var medf = parseInt(edf)/parseInt(month);
  document.getElementById('medf').value = Math.round(medf)
}


function calculateSalary(){

  // Changable Amount is travel allowance

  var arrears = document.getElementById("arr").value
  
  if(arrears == ""){
    arrears = parseInt(0)
    
  }
  else{
    arrears = parseInt(arrears)
    
  }
  
  var localRef = document.getElementById("lref").value
  if(localRef == ""){
    localRef = 0
  }
  else{
    localRef = parseInt(localRef)
  }
  
  var tfixAllow  = document.getElementById("falw").value
  if(tfixAllow == ""){
    tfixAllow = 0
  }
  else{
    tfixAllow = parseInt(tfixAllow)
  }

  var dfixAllow = document.getElementById("falw2").value
  if(dfixAllow == ""){
    dfixAllow = 0
  }
  else{
    dfixAllow = parseInt(dfixAllow)
  }

  var DiscBonus = document.getElementById("dbns").value
  if(DiscBonus == ""){
    DiscBonus = 0
  }
  else{
    DiscBonus = parseInt(DiscBonus)
  }

  var attBns = document.getElementById("atbns").value
  if(attBns == ""){
    attBns = 0
  }
  else{
    attBns = parseInt(attBns)
  }

  var transport1 = document.getElementById("tran").value
  if(transport1 == ""){
    transport1 = 0
  }
  else{
    transport1 = parseInt(transport1)
  }

  var transport2 = document.getElementById("tran2").value
  if(transport2 == ""){
    transport2 = 0
  }
  else{
    transport2 = parseInt(transport2)
  }

  var sick = document.getElementById("sref").value
  if(sick == ""){
    sick = 0
  }
  else{
    sick = parseInt(sick)
  }

  var speBns = document.getElementById("sbns").value
  if(speBns == ""){
    speBns = 0
  }
  else{
    speBns = parseInt(speBns)
  }

  var otherAllow = document.getElementById("oalw").value
  if(otherAllow == ""){
    otherAllow = 0
  }
  else{
    otherAllow = parseInt(otherAllow)
  }

  var otherDed = document.getElementById("oded").value
  if(otherDed == ""){
    otherDed = 0
  }
  else{
    otherDed = parseInt(otherDed)
  }

  var abs = document.getElementById("abs").value
  if(abs == ""){
    abs = 0
  }
  else{
    abs = parseInt(abs)
  }
  
  var ot1 = document.getElementById("am1").value
  if(ot1 == ""){
    ot1 = 0
  }
  else{
    ot1 = parseInt(ot1)
  }

  var ot2 = document.getElementById("am2").value
  if(ot2 == ""){
    ot2 = 0
  }
  else{
    ot2 = parseInt(ot2)
  }

  var ot3 = document.getElementById("am3").value
  if(ot3 == ""){
    ot3 = 0
  }
  else{
    ot3 = parseInt(ot3)
  }

  var lateness = document.getElementById("am4").value
  if(lateness == ""){
    lateness = 0
  }
  else{
    lateness = parseInt(lateness)
  }

  var tax = document.getElementById("amt1").value
  if(tax == ""){
    tax = 0
  }
  else{
    tax = parseInt(tax)
  }

  var ntax = document.getElementById("amt2").value
  if(ntax == ""){
    ntax = 0
  }
  else{
    ntax = parseInt(ntax)
  }
  
  var transport = parseInt(transport1) + parseInt(transport2)
  var overseas = parseInt(tax) + parseInt(ntax)
  
  var fixAllow = parseInt(tfixAllow) + parseInt(dfixAllow)
  var tbasic = document.getElementById("bsal").value
  var overtime = parseInt(ot1) + parseInt(ot2) +parseInt(ot3)
  var eoy = document.getElementById("eoy").value
  var speProBns = document.getElementById("spbonus3").value
  
  var loan = document.getElementById("lrep").value
  var paye = document.getElementById("paye").value
  var nps = document.getElementById("nps").value
  var nsf = document.getElementById("nsf").value
  var medical = document.getElementById("med2").value

  var edf = document.getElementById("edf").value
  var car = document.getElementById("car").value
  var slevy = document.getElementById("levy").value
  // alert(slevy)
  var educationRel = document.getElementById("edu").value
  var medicalRel = document.getElementById("mrel").value


  var pgross = document.getElementById("pgrs").value
  var piet = document.getElementById("piet").value
  var ppaye = document.getElementById("ppaye").value

  var basic = parseInt(tbasic) - parseInt(abs)


  var payable = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(transport) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(speBns) + parseInt(speProBns) + parseInt(fixAllow) + parseInt(DiscBonus) + parseInt(overseas) + parseInt(attBns)

  if(overseas > 0){
    ntax = Math.round(parseInt(basic) * 0.06)
    tax = Math.round(parseInt(overseas) - parseInt(ntax))
  }
  else{
    ntax = 0
    tax = 0
  }

  var cgross, grossTax
  var ptransport = 0
  var transTax
  if(transport > 20000){
    transTax = parseInt(transport) - 20000
  }
  else{
    transTax = 0
  }

  cgross = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(transport) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow) + parseInt(tax) + parseInt(speProBns) + parseInt(attBns) + parseInt(car)
  
  grossTax = parseInt(basic) + parseInt(overtime) + parseInt(transTax) + parseInt(otherAllow) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow) + parseInt(tax) + parseInt(speProBns) + parseInt(attBns) + parseInt(car)

  // var gtax = parseInt(cgross) + parseInt(transport)
  var gross = parseInt(pgross) + parseInt(grossTax)

  var tciet = parseInt(edf) + parseInt(medicalRel) + parseInt(educationRel)
  var ciet
  ciet = Math.round(parseInt(tciet) / 13)
  var iet = parseInt(ciet) + parseInt(piet)

  var netch = parseInt(gross) - parseInt(iet)
  if(netch < 0){
    netch = 0
  }
  else{
    netch = netch
  }

  var nps
  var cpaye
  var enps
  if(basic > 50000){
    nps = Math.round(parseInt(basic) * 0.03)
    // cpaye = Math.round(parseInt(netch) * 0.15)
    enps = Math.round(parseInt(basic) * 0.06)
  }
  else{
    nps = Math.round(parseInt(basic) * 0.015)
    // cpaye = Math.round(parseInt(netch) * 0.1)
    enps = Math.round(parseInt(basic) * 0.03)
  }

  if(edf < 700000){
    
    cpaye = Math.round(parseInt(netch) * 0.1)
  }
  else if(edf >=700000 && edf < 975000 ){
    
    cpaye = Math.round(parseInt(netch) * 0.125)
  }
  else{
    
    cpaye = Math.round(parseInt(netch) * 0.15)
  }

  if(cpaye < 0){
    cpaye = 0
  }
  else{
    cpaye = parseInt(cpaye)
  }

  if(ppaye < 0){
    ppaye = 0
  }
  else{
    ppaye = parseInt(ppaye)
  }

  paye = parseInt(cpaye) - parseInt(ppaye)

  if(paye < 0){
    paye = 0
  }
  else{
    paye = parseInt(paye)
  }
  
  nsf = Math.round(parseInt(basic) * 0.01)

  if(nsf > 214){
    nsf = 214
  }
  else{
    nsf = parseInt(nsf)
  }

  var temp = parseInt(cgross) * 13
  var slevy1
  var slevy2
  
  var pths = document.getElementById("ths2").value
  var plevy = document.getElementById("plevy").value

  var cths = 3000000 / 13
  var ths = parseInt(cths) + parseInt(pths)
  var netchar = parseInt(gross) - parseInt(iet) - parseInt(ths)
  if(temp > 3000000){
    slevy1 = Math.round(parseInt(netchar) * 0.25)
    slevy2 = Math.round(parseInt(grossTax) * 0.1)
    
    if(slevy1 > slevy2){
      slevy = Math.round(slevy2)
    }
    else{
      slevy = Math.round(slevy1)
    }
  }
  else{
    slevy = 0
  }
  var ensf = Math.round(parseInt(basic) * 0.025)
  if(ensf > 536){
    ensf = 536
  }
  else{
    ensf = Math.round(ensf)
  }
  var levy = Math.round(parseInt(basic) * 0.015)

  var deduction = parseInt(loan) + parseInt(paye) + parseInt(lateness) + parseInt(nps) + parseInt(otherDed) + parseInt(nsf) + parseInt(medical)

  var net = parseInt(payable) - parseInt(deduction)
  var pnet = parseInt(net) - parseInt(slevy)

  var ths = Math.round(3000000/13)
  var netchar = parseInt(gross) - parseInt(iet) - parseInt(ths)

  if(netchar <0){
    netchar = 0
  }
  else{
    netchar = netchar
  }

  // var clevy1 = parseInt(netchar) * 0.25
  // var clevy2 = parseInt(gross) * 0.1
  // var clevy
  // if(clevy1 > clevy2){
  //   clevy = Math.round(clevy2)
  // }
  // else{
  //   clevy = Math.round(clevy1)
  // }

  var eprgf
  var teprgf
  if(basic < 200000){
    teprgf = parseInt(basic) + parseInt(otherAllow) 
    eprgf = Math.round(teprgf * 0.035)
  }
  else{
    eprgf = 0
  }

  var levypay = parseInt(slevy) - parseInt(plevy)
  
  document.getElementById("bsal").value = basic
  document.getElementById("falw2").value = fixAllow
  document.getElementById("oded2").value = otherDed
  document.getElementById("ot2").value = overtime
  document.getElementById("dbns2").value = DiscBonus
  document.getElementById("nsf").value = nsf
  document.getElementById("oalw2").value = otherAllow
  document.getElementById("txdes2").value = tax
  document.getElementById("med2").value = medical
  document.getElementById("tran2").value = transport
  document.getElementById("ntxdes2").value = ntax
  document.getElementById("edf").value = edf
  document.getElementById("arr2").value = arrears
  document.getElementById("atbns2").value = attBns
  document.getElementById("eoy").value = eoy
  document.getElementById("lrep").value = loan
  document.getElementById("car").value = car
  document.getElementById("lref2").value = localRef
  document.getElementById("paye").value = paye
  // alert(slevy)
  document.getElementById("levy").value = levypay
  document.getElementById("spbonus2").value = speBns
  document.getElementById("late").value = lateness
  document.getElementById("edu").value = educationRel
  document.getElementById("spbonus3").value = speProBns
  document.getElementById("nps").value = nps
  document.getElementById("mrel").value = medicalRel
  document.getElementById("pay").value = payable
  document.getElementById("ded").value = deduction
  document.getElementById("pnet").value = pnet
  document.getElementById("npay").value = net
  document.getElementById("bsal2").value = basic
  document.getElementById("dbns3").value = DiscBonus
  // document.getElementById("cgrs").value = gtax
  document.getElementById("cgrs").value = grossTax
  document.getElementById("ot3").value = overtime
  document.getElementById("falw3").value = fixAllow
  document.getElementById("pgrs").value = pgross
  document.getElementById("oalw3").value = otherAllow
  document.getElementById("piet").value = piet
  document.getElementById("iet").value = iet  // check iet value
  document.getElementById("tran3").value = ptransport
  document.getElementById("txdes3").value = tax
  document.getElementById("netch").value = netch
  document.getElementById("arr3").value = arrears
  document.getElementById("spbonus3").value = speProBns
  document.getElementById("paye2").value = cpaye
  document.getElementById("eoy2").value = eoy
  document.getElementById("atbns3").value = attBns
  document.getElementById("ppaye").value = ppaye
  document.getElementById("lref3").value = localRef
  document.getElementById("car").value = car 
  document.getElementById("paye3").value = paye 
  document.getElementById("nps2").value = enps
  document.getElementById("nsf2").value = ensf
  document.getElementById("ivbt").value = levy
  document.getElementById("gtax").value = gross
  document.getElementById("prgf").value = eprgf

  document.getElementById("bsal3").value = basic
  document.getElementById("dbns4").value = DiscBonus
  document.getElementById("gtax2").value = grossTax
  document.getElementById("ot4").value = overtime
  document.getElementById("falw4").value = fixAllow
  document.getElementById("gtax3").value = gross
  document.getElementById("oalw4").value = otherAllow
  document.getElementById("piet2").value = piet
  document.getElementById("pgrs2").value = pgross
  document.getElementById("tran4").value = transport
  document.getElementById("txdes4").value = tax
  document.getElementById("iet2").value = iet
  document.getElementById("arr4").value = arrears
  document.getElementById("spbonus4").value = speProBns
  document.getElementById("ths").value = ths
  document.getElementById("eoy3").value = eoy
  document.getElementById("atbns4").value = attBns
  document.getElementById("ths2").value = pths
  document.getElementById("lref4").value = localRef
  document.getElementById("car2").value = car
  document.getElementById("netchar").value = netchar
  document.getElementById("clevy").value = slevy
  document.getElementById("plevy").value =plevy
  document.getElementById("levypay").value =levypay
  alert("Calculation Complete")
}

// Function For Export To Word File

function Export2Word(element, filename = 'paysheet'){
  var css = (
    '<style>' +
    '@page WordSection1{size: 1191pt 842pt;mso-page-orientation: landscape;}' +
    'div.WordSection1 {page: WordSection1;}' +
    'table{border-collapse:collapse;}td{border:1px gray solid;width:5em;padding:2px;}'+
    '</style>'
  );
 
  var preHtml = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
  var postHtml = "</body></html>";
  var html = preHtml+document.getElementById(element).innerHTML+postHtml;

  var blob = new Blob(['\ufeff', css + html], {
      type: 'application/msword'
  });
  
  // Specify link url
  var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html);
  
  // Specify file name
  filename = filename?filename+'.doc':'document.doc';
  
  // Create download link element
  var downloadLink = document.createElement("a");

  document.body.appendChild(downloadLink);
  
  if(navigator.msSaveOrOpenBlob ){
      navigator.msSaveOrOpenBlob(blob, filename);
  }else{
      // Create a link to the file
      downloadLink.href = url;
      
      // Setting the file name
      downloadLink.download = filename;
      
      //triggering the function
      downloadLink.click();
  }
  
  document.body.removeChild(downloadLink);
}
